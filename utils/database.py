from app.models import Product

def get_all_products():
    products = Product.query.all()
    return products