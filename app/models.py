from . import db

class Product(db.Model):
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stripe_product_id = db.Column(db.String(100), nullable=False)
    stripe_price_id = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<Product: {self.name}> - {self.description}>"


