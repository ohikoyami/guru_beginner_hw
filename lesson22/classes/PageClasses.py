import time

from selene import browser, have, be, by
from data.ponchik_info import Ponchik


class BasePage:
    def open(self):
        browser.should(have.title_containing('Krispy Kreme'))
        return self

    def logo_visibility(self):
        browser.element('.page-header-14__brand-logo').should(be.visible)
        return self


class CatalogPage:

    def check_ponchiki(self):
        browser.element('.product-section-info__header').should(have.text('Пончики'))
        browser.element('.product-section-info__up-content').should(have.text('Пончики Krispy Kreme'))
        return self

    def add_product_to_cart(self, ponchik: Ponchik):
        browser.element(by.xpath(f'.//*[@product-id="{ponchik.product_id}"]')).click()
        return self

    def open_product_card(self, ponchik: Ponchik):
        browser.element('.products-list-01-list>li').should(have.text(f'{ponchik.name}')).click()
        browser.element('.product-01').should(have.text(f'{ponchik.price}')).should(be.visible)
        return self

    def add_product_to_favorite_page(self):
        browser.element('.product-favorite').click()
        return self


class FavoritePage:

    def open(self):
        time.sleep(1)
        browser.element('.page-header-14__favorites').click()
        browser.element('.product-section-info__header').should(have.text('Избранное'))
        return self

    def check_added_product(self, ponchik: Ponchik):
        browser.element('.products-list-01__list-container').should(have.text(f'{ponchik.name}'))
        return self


class CartPage:
    def check_cart(self, ponchik: Ponchik):
        browser.element('[title="Корзина"]').should(be.visible).click()
        browser.element(by.name('cart.model.deliveryForm')).should(have.text('Корзина')).should(
            have.text(f'{ponchik.name}'))
        browser.element('.checkout-03-total-calc__count').should(have.text(f'{ponchik.price}'))
        return self


class ShopPonchiki:
    def __init__(self, ponchik: Ponchik):
        self.base_page = BasePage()
        self.catalog_page = CatalogPage()
        self.cart_page = CartPage()
        self.favorite_page = FavoritePage()
