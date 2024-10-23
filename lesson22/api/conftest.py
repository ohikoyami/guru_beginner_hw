import requests
import pytest


@pytest.fixture(scope='session')
def api_session():
    session = requests.Session()

    # Установка всех необходимых cookie
    cookies = {
        "_ga": "GA1.1.1917044127.1726598179",
        "_ym_uid": "1726594179328951185",
        "_ym_d": "1726594179328951185",
        "_session_id": "3cff22c06356c80252d87d1bf2d6bed0",
        "_ym_isad": "2",
        "_ga_JDK5KFCWPZ": "GS1.1.1729654582.5.0.1729655982.0.0.0",
        "_ga_7C63GEPMLM": "GS1.1.1729654567.6.1.1729657941.0.0.0"
    }

    for key, value in cookies.items():
        session.cookies.set(key, value)

    yield session  # Передаем сессию тестам

    session.close()