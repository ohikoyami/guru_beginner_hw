import requests

from data.site_data import FavoriteProduct

# Базовый URL для API Krispy Kreme
BASE_URL = "https://krispykreme-moskva.ru"


def update_favorite_product(product_id=4577827):
    """Обновляет продукт в избранном."""
    url = f"{BASE_URL}/favorite_products/44.json"
    payload = {
        "product_id": product_id
    }

    response = requests.put(url, json=payload)

    assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"


def add_in_favorite(product_id=44):
    """Добавляет продукт в избранное."""
    url = f"{BASE_URL}/favorite_products/{product_id}.json"
    data = FavoriteProduct(ID=str(product_id))

    response = requests.put(url, json=data.dict())

    assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"


def get_favorite_products():
    """Получает список избранных продуктов."""
    url = f"{BASE_URL}/favorite_products"
    response = requests.get(url)

    assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"
