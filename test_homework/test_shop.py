"""
Протестируйте классы из модуля test_homework/models.py
"""
import pytest

from test_homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """


    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(quantity=999) is True
        assert product.check_quantity(quantity=1000) is True
        assert product.check_quantity(quantity=1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(quantity=200)
        assert product.quantity == 800

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(quantity=1500)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, buy_count=1)
        assert cart.products[product] == 1

        cart.add_product(product, buy_count=2)
        assert cart.products[product] == 3

    def test_remove_product(self, product, cart):
        cart.add_product(product, buy_count=5)
        cart.remove_product(product, remove_count=1)
        assert cart.products[product] == 4
        cart.remove_product(product)
        assert product not in cart.products
        cart.add_product(product, buy_count=1)
        cart.remove_product(product, remove_count=3)
        assert product not in cart.products

    def test_clear(self, product, cart):
        cart.add_product(product, buy_count=5)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, cart, product):
        cart.add_product(product, buy_count=50)
        assert cart.get_total_price() == 5000
        cart.add_product(product, buy_count=20)
        assert cart.get_total_price() == 7000

    def test_buy_positive(self, cart, product):
        cart.add_product(product, buy_count=100)
        cart.add_product(product,  buy_count=200)
        cart.buy()
        assert product.quantity == 700

    def test_buy_negative(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, buy_count=1001)
            cart.buy()