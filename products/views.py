from flask import Blueprint, jsonify, request

from database import db
from products.models import Product, products_schema, product_schema

products = Blueprint('products', __name__)


@products.route('/')
def hello_world():
    return 'Hello World!'


@products.route('/products')
def get_products():
    all_products = Product.query.all()
    return jsonify({'data': products_schema.dump(all_products), 'success': True, 'message': 'Productos obtenidos'})


@products.route('/product/<int:id_product>')
def get_product(id_product):
    product = Product.query.get(id_product)
    if product is not None:
        return jsonify({'data': product_schema.dump(product), 'success': True, 'message': 'Producto obtenido'})
    else:
        return jsonify({'data': None, 'success': False, 'message': 'Producto no encontrado'})


@products.route('/product', methods=['POST'])
def insert_product():
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']
    new_product = Product(name, price, quantity)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'data': product_schema.dump(new_product), 'success': True, 'message': 'Producto agregado'})


@products.route('/product/<int:id_product>', methods=['PUT'])
def update_product(id_product):
    product = Product.query.get(id_product)

    if product is not None:
        product.name = request.json['name'] if 'name' in request.json else product.name
        product.price = request.json['price'] if 'price' in request.json else product.price
        product.quantity = request.json['quantity'] if 'quantity' in request.json else product.quantity
        db.session.commit()
        return jsonify({'data': product_schema.dump(product), 'success': True, 'message': 'Producto actualizado'})
    else:
        return jsonify({'data': None, 'success': False, 'message': 'Producto no encontrado'})


@products.route('/product/<int:id_product>', methods=['DELETE'])
def delete_product(id_product):
    product = Product.query.get(id_product)
    if product is not None:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'data': product_schema.dump(product), 'success': True, 'message': 'Producto eliminado'})
    else:
        return jsonify({'data': None, 'success': False, 'message': 'Producto no encontrado'})