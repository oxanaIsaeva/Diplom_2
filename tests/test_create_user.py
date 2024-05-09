import allure
import pytest
import requests
from data import Data


class TestCreateUser:
    accessToken = ''

    @allure.title('Проверка создания уникального пользователя')
    @allure.description('Запрос возвращает код ответа 200, и содержит "accessToken" и "refreshToken" в ответе')
    def test_create_user_positive(self):
        payload = Data.CREATE_USER
        response = requests.post(f'{Data.URL}/api/auth/register', data=payload)
        format_response = response.json()
        TestCreateUser.accessToken = format_response["accessToken"]

        assert (response.status_code == 200 and 'accessToken' in format_response.keys() and
                'refreshToken' in format_response.keys())

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Data.URL}/api/auth/user',
                        headers={"Authorization": TestCreateUser.accessToken})

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    @allure.description('Запрос возвращает код ответа 403 и ответ {"success": False, "message": "User already exists"}')
    def test_create_user_duplicate(self):
        payload = Data.CREATE_USER_DUPLICATE
        response = requests.post(f'{Data.URL}/api/auth/register', data=payload)
        format_response = response.json()

        assert (response.status_code == 403 and format_response == Data.RESPONSE_DUPLICATE_USER)

    @pytest.mark.parametrize(
        "variants",
        [
            {"password": "12345", "name": "Oxana2"},
            {"email": "test-Oxana2@yandex.ru", "name": "Oxana2"},
            {"email": "test-Oxana2@yandex.ru", "password": "12345"},
        ]
    )
    @allure.title('Проверка создания пользователя без одного из обязательных полей')
    @allure.description('Запрос возвращает код ответа 403 и ответ {"success": False, "message": '
                        '"Email, password and name are required fields"}')
    def test_create_user_negative(self, variants):
        payload = variants
        response = requests.post(f'{Data.URL}/api/auth/register', data=payload)
        format_response = response.json()

        assert (response.status_code == 403 and format_response == Data.RESPONSE_CREATE_USER_NEGATIVE)
