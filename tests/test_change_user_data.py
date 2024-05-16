import allure
import pytest
import requests
from data import Data
from conftest import create_new_user


class TestChangeUserData:

    @allure.title('Проверка изменения электронной почты пользователя с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "user" в ответе')
    def test_change_user_email(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = Data.USER_CHANGE_EMAIL
        response = requests.patch(f'{Data.URL}/api/auth/user',
                                  headers={"Authorization": token},
                                  data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'user' in format_response.keys())

    @allure.title('Проверка изменения имени пользователя с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "user" в ответе')
    def test_change_user_name(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = Data.USER_CHANGE_NAME
        response = requests.patch(f'{Data.URL}/api/auth/user',
                                  headers={"Authorization": token},
                                  data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'user' in format_response.keys())

    @allure.title('Проверка изменения пароля пользователя с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "user" в ответе')
    def test_change_user_password(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = Data.USER_CHANGE_PASSWORD
        response = requests.patch(f'{Data.URL}/api/auth/user',
                                  headers={"Authorization": token},
                                  data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'user' in format_response.keys())

    @pytest.mark.parametrize(
        "variants",
        [
            {"email": "test-OxanaNegavive@yandex.ru"},
            {"name": "OxanaNegative"},
            {"password": "Negative12345"}
        ]
    )
    @allure.title('Проверка изменения данных пользователя без авторизации')
    @allure.description('Запрос возвращает код ответа 401, и {"success": False, "message": "You should be authorised"}'
                        ' в ответе')
    def test_change_user_data_negative(self, variants):
        payload = variants
        response = requests.patch(f'{Data.URL}/api/auth/user',
                                  data=payload)
        format_response = response.json()

        assert (response.status_code == 401 and format_response == Data.RESPONSE_UPDATE_USER_DATA_NEGATIVE)

    @allure.title('Проверка изменения электронной почты пользователя на почту, которая уже используется')
    @allure.description('Запрос возвращает код ответа 403, и {"success": False, "message": "User with such email '
                        'already exists"} в ответе')
    def test_change_user_email_negative(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = Data.USER_CHANGE_EMAIL_NEGATIVE
        response = requests.patch(f'{Data.URL}/api/auth/user',
                                  headers={"Authorization": token},
                                  data=payload)
        format_response = response.json()

        assert (response.status_code == 403 and format_response == Data.RESPONSE_UPDATE_USER_EMAIL_NEGATIVE)
