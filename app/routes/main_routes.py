import stripe
from flask import current_app, jsonify, render_template, request, Blueprint


routes_bp = Blueprint("routes_bp", __name__)


@routes_bp.route("/")
def index():
    return render_template("index.html")

@routes_bp.route("/hello")
def hello_world():
    return jsonify("hello, world!")

@routes_bp.route("/config")
def get_publishable_key():
    stripe_publishable_key = current_app.config['STRIPE_PUBLISHABLE_KEY']
    stripe_config = {"public_key": stripe_publishable_key}
    return jsonify(stripe_config)

@routes_bp.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
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
                    "price": "price_1PEzaMRwa8DwDjSVhzZ0LMZS",
                    "quantity": 1
                }
            ]
        )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        return jsonify(error=str(e)), 403

@routes_bp.route("/success")
def success():
    return render_template("success.html")

@routes_bp.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")

@routes_bp.route("/payment-webhook", methods=["POST"])
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
