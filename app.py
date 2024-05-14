import os

import stripe
from flask import Flask, jsonify, render_template

app = Flask(__name__)

stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
}


stripe.api_key = stripe_keys["secret_key"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello_world():
    return jsonify("hello, world!")

@app.route("/config")
def get_publishable_key():
    stripe_config = {"public_key": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = stripe_keys["secret_key"]
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


if __name__ == "__main__":
    app.run()