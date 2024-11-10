import allure
from allure_commons.types import Severity

from lesson22.classes.api.PageClasses_API import Cart, Favorite
from lesson22.products.raspberry_pistachio_shell import raspberry_pistachio_shell

cart = Cart()
favorite = Favorite()


@allure.tag('api')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности корзины')
@allure.title('Проверка добавления пончика в корзину и обновление количества')
def test_cart_api(api_session):
    with allure.step('Добавление пончика в корзину'):
        cart.add_product_to_cart(raspberry_pistachio_shell, api_session)
    with allure.step('Обновление количества пончика в корзине'):
        cart.update_product_quantity(raspberry_pistachio_shell, api_session)
    with allure.step('Получение данных корзины и проверка результата'):
        cart.get_cart_data(api_session)


@allure.tag('api')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'bilenkoda')
@allure.feature('Проверка сайта krispykreme')
@allure.story('Тест функциональности избранного')
@allure.title('Проверка добавления пончика в избранное и обновление избранного')
def test_favorite_api(api_session):
    with allure.step('Добавление пончика в избранное'):
        favorite.add_in_favorite(raspberry_pistachio_shell, api_session)
    with allure.step('Обновление пончика в избранном'):
        favorite.update_favorite_product(raspberry_pistachio_shell, api_session)
    with allure.step('Получение списка избранных продуктов и проверка результата'):
        favorite.get_favorite_products(api_session)
