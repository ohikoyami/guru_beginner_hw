import requests

def test_get_cart_data():
    url = "https://krispykreme-moskva.ru/product_cart.json?where=productSection"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "X-CSRF-Token": "GD2/hOA7xZCxiD/FYxSrjiFeHKg33GeYGXsDaPfCBikAHhxSN/ivvdebQAZ9bq5CDhEszhaFWQs0GPdAhKnJkQ=="
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "Expected status code 200"
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Unexpected content type"
    assert response.json() is not None, "Response should not be None"

def test_get_donuts_page():
    url = "https://krispykreme-moskva.ru/ponchiki"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200, "Expected status code 200"
    assert "Пончики" in response.text, "Expected 'Пончики' in the page content"
    assert '_session_id' in response.cookies, "Expected session cookie to be set"


def test_update_product_quantity():
    url = "https://krispykreme-moskva.ru/product_cart/update_quantity.json"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Cookie": "_session_id=3cff22c06356c80252d87d1bf2d6bed0; _ga=GA1.1.1917044127.1726594179; _ym_uid=1726594179328951185; _ym_d=1726594179; _ym_isad=2; _ga_JDK5KFCWPZ=GS1.1.1729654582.5.0.1729655982.0.0.0; _ga_7C63GEPMLM=GS1.1.1729654567.6.1.1729656988.0.0.0",
        "Origin": "https://krispykreme-moskva.ru",
    }

    payload = {
        "product_id": 4577827,  # ID продукта, который нужно обновить
        "quantity": 2  # Новое количество
    }

    response = requests.put(url, json=payload, headers=headers)

    # Проверка ответа
    if response.status_code == 200:
        print("Количество продукта успешно обновлено.")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

def test_update_favorite_product():
    url = f"https://krispykreme-moskva.ru/favorite_products/44.json"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Cookie": "_session_id=3cff22c06356c80252d87d1bf2d6bed0; _ga=GA1.1.1917044127.1726594179; _ym_uid=1726594179328951185; _ym_d=1726594179; _ym_isad=2; _ga_JDK5KFCWPZ=GS1.1.1729654582.5.0.1729655982.0.0.0; _ga_7C63GEPMLM=GS1.1.1729654567.6.1.1729657941.0.0.0",
        "Origin": "https://krispykreme-moskva.ru",
        "x-csrf-token": "nnEDCfDqzOF04n8GK2V5SnMsq3ZhLVzh5unBYlAV2rGGUqDfJymmzBLxAMU1H3yGXGObEEB0YnLLijVKI34VCQ=="
    }

    payload = {
        "product_id": 4577827
    }

    response = requests.put(url, json=payload, headers=headers)

    # Проверка ответа
    if response.status_code == 200:
        print("Продукт успешно обновлен в избранном.")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

def test_get_favorite_products():
    url = "https://krispykreme-moskva.ru/favorite_products"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Cookie": "_ga=GA1.1.1917044127.1726598179; _ym_uid=1726594179328951185; _ym_d=1726594179328951185; _session_id=3cff22c06356c80252d87d1bf2d6bed0; _ym_isad=2; _ga_JDK5KFCWPZ=GS1.1.1729654582.5.0.1729655982.0.0.0; _ga_7C63GEPMLM=GS1.1.1729654567.6.1.1729657941.0.0.0"
    }

    response = requests.get(url, headers=headers)

    # Проверка ответа
    if response.status_code == 200:
        print("Список избранных продуктов успешно получен.")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")