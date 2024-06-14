import stripe
from flask import current_app, jsonify, request, Blueprint


stripe_bp = Blueprint("stripe_bp", __name__)


@stripe_bp.route("/hello")
def hello_world():
    return jsonify("hello, world!")

@stripe_bp.route("/config")
def get_publishable_key():
    stripe_publishable_key = current_app.config['STRIPE_PUBLISHABLE_KEY']
    stripe_config = {"public_key": stripe_publishable_key}
    return jsonify(stripe_config)


@stripe_bp.route("/create-checkout-session", methods=['POST'])
def create_checkout_session():
    data = request.json
    price_id = data['price_id']
    domain_url = current_app.config['BASE_URL']
    stripe_secret_key = current_app.config['STRIPE_SECRET_KEY']
    stripe.api_key = stripe_secret_key
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {                   
                    "price": price_id,
                    "quantity": 1
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

@stripe_bp.route("/payment-webhook", methods=["POST"])
def payment_webhook():
    payload = request.get_data(as_text=True)
    signature_header = request.headers.get("Stripe-Signature")
    stripe_secret_key = current_app.config['STRIPE_SECRET_KEY']
    webhook_secret = current_app.config['STRIPE_WEBHOOK_SECRET']

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, stripe_secret_key
        )
    except ValueError as e:
        # Invalid payload
        return jsonify(error=str(e)), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify(error=str(e)), 400
    
    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Checkout completed successfully!")
        # TODO: add code to update order status and send emails
    elif event["type"] == "checkout.session.canceled":
        print("Uh-oh, checkout canceled")
        # TODO: add code to update order status and send emails
    return "Success", 200
