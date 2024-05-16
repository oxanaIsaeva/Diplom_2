import allure
import pytest
import requests
from data import Data
from conftest import create_new_user


class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "order" в ответе')
    def test_create_order_with_authorization(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = Data.INGREDIENTS
        response = requests.post(f'{Data.URL}/api/orders',
                                 headers={"Authorization": token},
                                 data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'order' in format_response.keys())

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "order" в ответе')
    def test_create_order_wo_authorization(self):
        payload = Data.INGREDIENTS
        response = requests.post(f'{Data.URL}/api/orders',
                                 data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'order' in format_response.keys())

    @allure.title('Проверка создания заказа с невалидным хешем ингредиента')
    @allure.description('Запрос возвращает код ответа 500, и содержит "Internal Server Error" в ответе')
    def test_create_order_with_invalid_hash(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = {"ingredients": ["60d3b41abdooob0026a733c6"]}
        response = requests.post(f'{Data.URL}/api/orders',
                                 headers={"Authorization": token},
                                 data=payload)

        assert (response.status_code == 500 and response.reason == "Internal Server Error")

    @pytest.mark.parametrize(
        "body",
        [
            {"ingredients": [""]},
            {"ingredients": []},
            ''
        ]
    )
    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Запрос возвращает код ответа 400 и ответ {"success": False, "message": "Ingredient ids must '
                        'be provided"}')
    def test_create_order_wo_ingredients(self, body, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        payload = body
        response = requests.post(f'{Data.URL}/api/orders',
                                 headers={"Authorization": token},
                                 data=payload)
        format_response = response.json()

        assert (response.status_code == 400 and format_response == Data.RESPONSE_CREATE_ORDER_NEGATIVE)
