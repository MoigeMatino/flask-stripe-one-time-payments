from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend_bp', __name__)

@frontend_bp.route("/")
def index():
    return render_template("index.html")

@frontend_bp.route('/products')
def add_product_view():
    return render_template('add_product.html')

@frontend_bp.route("/success")
def success():
    return render_template("success.html")

@frontend_bp.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")
