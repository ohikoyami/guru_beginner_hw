from allure_commons._allure import step
from selene import browser, have, be

from config.config import BASE_URL, LOGIN
from products.products_info import (
    auth_cookie,
    remove_all_products_from_cart,
    check_cart_num_of_products_ui,
    check_cart_add_correct_products_ui,
    Product,
    product_laptop
)


def test_login():
    with step('Open Main Page'):
        browser.open(BASE_URL)

    with step('Set cookie from API'):
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_cookie().get('NOPCOMMERCE.AUTH')})

    with step('Open main page'):
        browser.open(BASE_URL)

    with step('Verify successful authorization'):
        browser.element(".account").should(have.text(LOGIN))

    with step('Close browser'):
        browser.quit()


def test_add_product_to_cart():

    with step('Open Main Page'):
        browser.open(BASE_URL)

    with step('Set cookie from API'):
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_cookie().get('NOPCOMMERCE.AUTH')})

    with step('Refresh status main page'):
        browser.driver.refresh()

    with step('Remove all products from cart'):
        remove_all_products_from_cart()

    with step('Add Laptop'):
        Product.add_product_to_cart(product_laptop)

    with step('Check number of products in cart'):
        check_cart_num_of_products_ui(product_laptop.product_quantity)

    # Проверка, что продукт корректно добавлен в корзину
    with step('Check correct info of added products in cart'):
        check_cart_add_correct_products_ui(product_laptop.product_quantity, product_laptop.product_name)


def test_logout():
    with step('Open Main Page'):
        browser.open(BASE_URL)

    with step('Set cookie from API'):
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': auth_cookie().get('NOPCOMMERCE.AUTH')})

    with step('Refresh status main page'):
        browser.driver.refresh()

    with step('Logout'):
        browser.element('.ico-logout').click()

    with step('Verify successful logout'):
        browser.element('.ico-login').should(be.visible)

    with step('Close browser'):
        browser.quit()
