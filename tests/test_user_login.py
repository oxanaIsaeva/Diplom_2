import allure
import pytest
import requests
from data import Data


class TestUserLogin:

    @allure.title('Проверка логина под существующим пользователем')
    @allure.description('Запрос возвращает код ответа 200, и содержит "accessToken", "refreshToken" и "user" в '
                        'ответе')
    def test_user_login_positive(self):
        payload = Data.LOGIN_USER
        response = requests.post(f'{Data.URL}/api/auth/login', data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'accessToken' in format_response.keys() and
                'refreshToken' and "user" in format_response.keys())

    @pytest.mark.parametrize(
        "variants",
        [
            {"email": "test-Oxana2@yandex.ru", "password": "incorrect"},
            {"email": "incorrect", "password": "incorrect"},
            {"email": "test-Oxana2@yandex.ru"},
            {"password": "12345"},
            {"email": "", "password": ""},
            {}
        ]
    )
    @allure.title('Проверка логина с неверным логином и паролем')
    @allure.description('Запрос возвращает код ответа 401 и ответ {"success": False, "message": "email or password '
                        'are incorrect"}')
    def test_user_login_negative(self, variants):
        payload = variants
        response = requests.post(f'{Data.URL}/api/auth/login', data=payload)
        format_response = response.json()

        assert (response.status_code == 401 and format_response == Data.RESPONSE_USER_LOGIN_NEGATIVE)
