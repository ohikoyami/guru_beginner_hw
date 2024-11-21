import requests
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"


@allure.feature("Post API Tests")
@allure.story("Testing CRUD operations on posts")
def test_get_posts():
    with allure.step("Get all posts"):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)  # Проверяем, что ответ - это список
        assert len(response.json()) > 0  # Проверяем, что список не пустой


@allure.feature("Post API Tests")
@allure.story("Creating a new post")
def test_create_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    with allure.step("Create a new post"):
        response = requests.post(f"{BASE_URL}/posts", json=new_post)
        assert response.status_code == 201
        assert response.json()["title"] == new_post["title"]
        assert response.json()["body"] == new_post["body"]


@allure.feature("Post API Tests")
@allure.story("Updating an existing post")
def test_update_post():
    updated_post = {
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    with allure.step("Update the post"):
        response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
        assert response.status_code == 200
        assert response.json()["title"] == updated_post["title"]
        assert response.json()["body"] == updated_post["body"]


@allure.feature("Post API Tests")
@allure.story("Deleting a post")
def test_delete_post():
    # Проверяем, что пост существует
    with allure.step("Get the post to ensure it exists"):
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200  # Проверяем, что пост есть

    # Удаляем пост
    with allure.step("Delete the post"):
        response = requests.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200  # Проверяем, что удаление прошло успешно

    # Проверяем, что пост все еще существует
    with allure.step("Get the post again to verify it still exists"):
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200  # Убедитесь, что можно получить пост
