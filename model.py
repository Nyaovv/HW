from datetime import datetime

from pony.orm import (
    Database, Required, Optional, Set, PrimaryKey
)


db = Database()


class Product(db.Entity):
    """Товар"""
    category = Required('Category')
    title = Required(str)
    description = Optional(str)
    unit = Required(str)
    price = Required(float)
    # alt_categories = Set('Category')
    # amount = int # сколько товаров в магазине сейчас
    history = Set('ProductHistory')


class ProductHistory(db.Entity):
    product = Required('Product')
    created = Optional(datetime, default=datetime.now)
    price = Required(float)


class Category(db.Entity):
    """Категория товара"""
    title = Required(str)
    products = Set('Product')

class Customer(db.Entity):
    """Покупатель"""
    email = Required(str)
    phone = Required(str)
    name = Required(str)
    addresses = Set('Address')

class Address(db.Entity):
    """Адрес"""
    customer = Set('Customer')
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(int)

class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Set('Customer')
    products = Set(list('CartItem'))

class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Set('Cart')
    product = Set('Product')
    amount = Optional(int)  # 1 единица товара

class Order(db.Entity):
    """Заказ"""
    customer = Set('Customer')
    created = Required(datetime)
    products = Set(list('OrderItem'))
    status = Set('Status')

class Status(db.Entity):
    """Статус"""
    name = Required(str)

class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Set('Order')
    product = Set('Product')
    amount = Optinal(int) # 1 единица товара

class Menu(db.Entity):
    """Меню"""
    pass
