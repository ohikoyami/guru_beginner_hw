from data.site_data import CartResponse, Ponchik, FavoriteProduct


class Cart:
    def __init__(self):
        self.base_url = "https://krispykreme-moskva.ru"

    def get_cart_data(self, api_session):  # Добавлен параметр api_session
        url = f"{self.base_url}/product_cart.json"
        response = api_session.get(url)  # Используем api_session вместо requests

        assert response.status_code == 200, "Ожидаемый код статуса 200"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Неожиданный тип контента"
        cart_data = CartResponse.parse_obj(response.json())
        assert cart_data.products is not None, "Ответ не должен быть None"

    def update_product_quantity(self, ponchik: Ponchik, api_session):
        url = f"{self.base_url}/product_cart/update_quantity.json"

        payload = {
            "product_id": ponchik.product_id,
            "quantity": ponchik.quantity + 1
        }

        response = api_session.put(url, json=payload)

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"

    def add_product_to_cart(self, ponchik: Ponchik, api_session):
        url = f"{self.base_url}/product_cart/add.json"

        payload = {
            "id": ponchik.product_id,
            "name": ponchik.name,
            "price": ponchik.price,
            "category": ponchik.category,
            "quantity": ponchik.quantity
        }

        # Отправка запроса
        response = api_session.put(url, json=payload)

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"


class Favorite:

    def __init__(self):
        self.base_url = "https://krispykreme-moskva.ru"

    def update_favorite_product(self, ponchik: Ponchik, api_session):
        """Обновляет продукт в избранном."""
        url = f"{self.base_url}/favorite_products/44.json"
        payload = {
            "product_id": ponchik.product_id
        }

        response = api_session.put(url, json=payload)

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"

    def add_in_favorite(self, ponchik: Ponchik, api_session):
        """Добавляет продукт в избранное."""
        url = f"{self.base_url}/favorite_products/{ponchik.add_id}.json"
        data = FavoriteProduct(ID=str(ponchik.add_id))

        response = api_session.put(url, json=data.dict())

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"

    def get_favorite_products(self, api_session):  # Добавлен параметр api_session
        """Получает список избранных продуктов."""
        url = f"{self.base_url}/favorite_products"
        response = api_session.get(url)  # Используем api_session вместо requests

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"
