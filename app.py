import os

import stripe
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

publishable_key = os.getenv("STRIPE_PUBLISHABLE_KEY")
secret_key = os.getenv("STRIPE_SECRET_KEY")
webhook_secret = os.getenv("STRIPE_ENDPOINT_SECRET")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello_world():
    return jsonify("hello, world!")

@app.route("/config")
def get_publishable_key():
    # publishable_key = os.getenv["STRIPE_PUBLISHABLE_KEY"]
    stripe_config = {"public_key": publishable_key }
    return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
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

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")

@app.route("/payment-webhook", methods=["POST"])
def payment_webhook():
    payload = request.get_data(as_text=True)
    signature_header = request.headers.get("Stripe-Signature")
    
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, secret_key
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


if __name__ == "__main__":
    app.run()