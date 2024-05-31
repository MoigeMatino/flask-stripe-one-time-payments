import uuid
from sqlalchemy.dialects.postgresql import UUID
from . import db

class Product(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stripe_product_id = db.Column(db.String(100), nullable=False)
    stripe_price_id = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<Product: {self.name}> - {self.description}>"


