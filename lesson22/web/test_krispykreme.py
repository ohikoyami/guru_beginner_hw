from selene import browser
import allure
from allure_commons.types import Severity
from products.raspberry_pistachio_shell import raspberry_pistachio_shell
from classes.PageClasses import ShopPonchiki

shop_ponchiki = ShopPonchiki()


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.step('Проверка тайтла главной страницы сайта')
def test_open_base_page():
    shop_ponchiki.base_page.open()

@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.step('Проверка лого главной страницы сайта')
def test_logo_visibility():
    shop_ponchiki.base_page.logo_visibility()

@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.step('Проверка открытия католога с пончиками')
def test_ponchik_on_catalog_page():
    browser.open('/ponchiki')
    shop_ponchiki.catalog_page.check_ponchiki()

@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.step('Проверка добавления поника в корзину')
def test_add_to_cart():
    browser.open('/ponchiki')
    shop_ponchiki.catalog_page.add_product_to_cart(raspberry_pistachio_shell)
    shop_ponchiki.cart_page.check_cart(raspberry_pistachio_shell)

@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.step('Проверка добавления поника в избранное')
def test_add_to_favorite():
    browser.open('/ponchiki')
    shop_ponchiki.catalog_page.open_product_card(raspberry_pistachio_shell).add_product_to_favorite_page()
    shop_ponchiki.favorite_page.open().check_added_product(raspberry_pistachio_shell)
