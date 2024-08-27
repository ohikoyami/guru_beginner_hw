"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from lesson8.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1500) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(300)
        assert product.quantity == 700

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match="Продуктов не хватает"):
            product.buy(1500)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

    def test_cart_add_more_one_product(self, cart, product):
        cart.add_product(product, 6)
        cart.add_product(product, 5)
        assert cart.products[product] == 11

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 6)
        assert cart.products[product] == 4

    def test_cart_remove_product_without_remove_count(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_remove_product_more_than_in_cart(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product, 5)
        assert product not in cart.products

    def test_cart_remove_all_product(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product, 5)
        assert product not in cart.products

    def test_cart_clear(self, cart, product):
        cart.add_product(product, 5)
        cart.clear()
        assert cart.products == {}

    def test_cart_get_total_price(self, cart, product):
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

    def test_cart_buy_less_than_in_storage(self, cart, product):
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 995
        assert cart.products == {}

    def test_cart_buy_same_in_storage(self, cart, product):
        cart.add_product(product, 1000)
        cart.buy()
        assert product.quantity == 0
        assert cart.products == {}

    def test_cart_buy_more_than_in_storage(self, cart, product):
        cart.add_product(product, 1500)
        with pytest.raises(ValueError, match="Нет такого количества товара на складе"):
            cart.buy()
