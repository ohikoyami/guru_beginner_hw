import requests
import allure
import pytest

# Базовый URL GitHub API
BASE_URL = "https://api.github.com"

@allure.feature('GitHub API')
@allure.story('Получение информации о пользователе')
@allure.step("Тест на получение информации о пользователе {username}")
def test_get_user_info(username="ohikoyami"):
    with allure.step(f"Отправка запроса на получение информации о пользователе {username}"):
        response = requests.get(f"{BASE_URL}/users/{username}")

    with allure.step("Проверка, что статус ответа 200"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    with allure.step("Проверка структуры ответа"):
        data = response.json()
        assert "login" in data, "Login field is missing in the response"
        assert data["login"] == username, f"Expected username {username}, got {data['login']}"


@allure.feature('GitHub API')
@allure.story('Проверка публичных репозиториев пользователя')
@allure.step("Тест на получение репозиториев пользователя {username}")
def test_get_user_repos(username="ohikoyami"):
    with allure.step(f"Отправка запроса на получение публичных репозиториев пользователя {username}"):
        response = requests.get(f"{BASE_URL}/users/{username}/repos")

    with allure.step("Проверка, что статус ответа 200"):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    with allure.step("Проверка наличия репозиториев"):
        repos = response.json()
        assert isinstance(repos, list), "Expected repos to be a list"
        assert len(repos) > 0, "Expected at least one repository"


@allure.feature('GitHub API')
@allure.story('Проверка несуществующего пользователя')
@allure.step("Тест на запрос информации несуществующего пользователя {username}")
def test_nonexistent_user(username="ohikoyamiiiii"):
    with allure.step(f"Отправка запроса на получение информации о несуществующем пользователе {username}"):
        response = requests.get(f"{BASE_URL}/users/{username}")

    with allure.step("Проверка, что статус ответа 404"):
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
