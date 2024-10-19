import requests
import allure

BASE_URL = 'https://api.github.com'


@allure.feature('GitHub API')
@allure.story('Получение информации о пользователе')
@allure.step("Тест на получение информации о пользователе")
def test_get_user_info():
    pass
