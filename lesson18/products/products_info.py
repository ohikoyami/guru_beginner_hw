import logging
import requests
from allure_commons.types import AttachmentType
from selene import browser, be, have, query
from config.config import BASE_URL, LOGIN, PASSWORD


class Product:
    def __init__(self, product_id, product_quantity, product_name):
        self.product_id = product_id
        self.product_quantity = product_quantity
        self.product_name = product_name

    def add_product_to_cart(self):
        url = f"{BASE_URL}/addproducttocart/catalog/{self.product_id}/{self.product_quantity}/1"
        response = requests.post(url, cookies=auth_cookie())
        browser.driver.refresh()
        browser.element('.cart-qty').should(be.visible).should(have.text(f'({self.product_quantity})'))
        attach(body=response.request.url, name='Request', attachment_type=AttachmentType.TEXT,
                           extension="txt")
        attach(body=json.dumps(dict(response.request.headers),
                           indent=4, ensure_ascii=True), name='Request Headers',
        attachment_type=AttachmentType.JSON,
                           extension="json")
        attach(body=json.dumps(response.json(),
                           indent=4, ensure_ascii=True), name="Response", attachment_type=AttachmentType.JSON,
                           extension="json")
        attach(body=str(response.cookies.get('Nop.customer')), name="Cookies", attachment_type=AttachmentType.TEXT,
                           extension="txt")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
        return response


def auth_cookie():
    response = requests.post(
        url=f"{BASE_URL}/login",
        data={'Email': LOGIN, 'Password': PASSWORD, 'RememberMe': False},
        allow_redirects=False
    )
    auth = dict()
    auth['NOPCOMMERCE.AUTH'] = response.cookies.get('NOPCOMMERCE.AUTH')
    return auth


def check_cart_add_correct_products_ui(product_quantity, product_name):
    browser.open(f"{BASE_URL}/cart")

    product_name_in_cart = browser.element('.product-name')
    product_name_in_cart.should(have.text(f'{product_name}'))

    quantity_input = browser.element('.product-name').element('./ancestor::tr/td[5]//input[@class="qty-input"]')
    quantity_input.should(have.value(f'{product_quantity}'))


def check_cart_num_of_products_ui(total_quantity):
    check_quantity_status()


def remove_product_from_cart():
    browser.open(BASE_URL + '/cart')
    browser.element('[name="removefromcart"]').click()
    browser.element('[name="updatecart"]').click()


def remove_all_products_from_cart():
    browser.open(BASE_URL + '/cart')

    while True:
        quantity_status = check_quantity_status()

        if quantity_status != 0:
            remove_product_from_cart()
        else:
            break

    browser.element('.cart-qty').should(be.visible).should(have.text(f'(0)'))


def check_quantity_status():
    cart_quantity = browser.element('.cart-qty').should(be.visible).get(query.text)
    quantity_in_cart = int(cart_quantity.strip('()'))
    return quantity_in_cart


# Продукты
product_laptop = Product(31, 1, '14.1-inch Laptop')
