from database import db, ma


class Product(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'price', 'quantity')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)