import requests
import pytest


@pytest.fixture(scope='session')
def api_session():
    session = requests.Session()

    # Установка всех необходимых cookie
    cookies = {
        "_session_id": "3cff22c06356c80252d87d1bf2d6bed0",
    }

    for key, value in cookies.items():
        session.cookies.set(key, value)

    yield session  # Передаем сессию тестам

    session.close()