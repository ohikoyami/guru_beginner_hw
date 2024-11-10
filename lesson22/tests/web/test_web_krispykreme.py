from allure_commons._allure import step
from selene import browser
import allure
from allure_commons.types import Severity
from lesson22.products.raspberry_pistachio_shell import raspberry_pistachio_shell
from lesson22.classes.web.PageClasses_web import ShopPonchiki

shop_ponchiki = ShopPonchiki()


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.title('Проверка тайтла главной страницы сайта')
def test_open_base_page():
    shop_ponchiki.base_page.open()


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.title('Проверка лого главной страницы сайта')
def test_logo_visibility():
    shop_ponchiki.base_page.logo_visibility()


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.title('Проверка открытия католога с пончиками')
def test_ponchik_on_catalog_page():
    with step('Открытие страницы с пончиками'):
        browser.open('/ponchiki')
    with step('Открытие страницы пончика в каталоге'):
        shop_ponchiki.catalog_page.check_ponchiki()


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.title('Проверка добавления поника в корзину')
def test_add_to_cart():
    with step('Открытие страницы с пончиками'):
        browser.open('/ponchiki')
    with step('Добавление пончика в корзину'):
        shop_ponchiki.catalog_page.add_product_to_cart(raspberry_pistachio_shell)
    with step('Проверка, что нужный пончик действительно добавлен в корзину'):
        shop_ponchiki.cart_page.check_cart(raspberry_pistachio_shell)


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности сайта')
@allure.title('Проверка добавления поника в избранное')
def test_add_to_favorite():
    with step('Открытие страницы с пончиками'):
        browser.open('/ponchiki')
    with step('Добавление пончика в избранное'):
        shop_ponchiki.catalog_page.open_product_card(raspberry_pistachio_shell).add_product_to_favorite_page()
    with step('Проверка, что нужный пончик действительно добавлен в избранное'):
        shop_ponchiki.favorite_page.open().check_added_product(raspberry_pistachio_shell)
