import requests

from data.site_data import CartResponse, Product


class Cart:
    def __init__(self):
        self.base_url = "https://krispykreme-moskva.ru"

    def get_cart_data(self):
        """Получает данные корзины через API."""
        url = f"{self.base_url}/product_cart.json"
        response = requests.get(url)

        assert response.status_code == 200, "Ожидаемый код статуса 200"
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Неожиданный тип контента"
        cart_data = CartResponse.parse_obj(response.json())
        assert cart_data.products is not None, "Ответ не должен быть None"

    def update_product_quantity(self, product_id=4577827, quantity=2):
        """Обновляет количество продукта в корзине."""
        url = f"{self.base_url}/product_cart/update_quantity.json"

        payload = {
            "product_id": product_id,
            "quantity": quantity
        }

        response = requests.put(url, json=payload)

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"

    def add_to_cart(self, product_id=4577827, name="Шелл малиново-фисташковый", price=170, quantity="min"):
        """Добавляет продукт в корзину."""
        url = f"{self.base_url}/product_cart/add.json"

        payload = Product(id=str(product_id), name=name, price=price, category="Пончики", quantity=quantity)

        response = requests.put(url, json=payload.dict())

        assert response.status_code == 200, f"Ожидаемый код статуса 200, получен {response.status_code}"


cart = Cart()
