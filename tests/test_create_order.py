import allure
import pytest
import requests
from data import Data


class TestCreateOrder:
    accessToken = ''
    ingredients = []

    @classmethod
    def setup_class(cls):
        payload = Data.CREATE_USER
        response = requests.post(f'{Data.URL}/api/auth/register', data=payload)
        format_response = response.json()
        TestCreateOrder.accessToken = format_response["accessToken"]

        response_ingredients = requests.get(f'{Data.URL}/api/ingredients')
        format_response_ingredients = response_ingredients.json()
        list_of_ingredients = format_response_ingredients["data"]
        ingredient_1 = list_of_ingredients[0]
        ingredient_2 = list_of_ingredients[3]
        ingredient_3 = list_of_ingredients[5]
        TestCreateOrder.ingredients.append(ingredient_1["_id"])
        TestCreateOrder.ingredients.append(ingredient_2["_id"])
        TestCreateOrder.ingredients.append(ingredient_3["_id"])

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "order" в ответе')
    def test_create_order_with_authorization(self):
        payload = {"ingredients": TestCreateOrder.ingredients}
        response = requests.post(f'{Data.URL}/api/orders',
                                 headers={"Authorization": TestCreateOrder.accessToken},
                                 data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'order' in format_response.keys())

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "order" в ответе')
    def test_create_order_wo_authorization(self):
        payload = {"ingredients": TestCreateOrder.ingredients}
        response = requests.post(f'{Data.URL}/api/orders',
                                 data=payload)
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'order' in format_response.keys())

    @allure.title('Проверка создания заказа с невалидным хешем ингредиента')
    @allure.description('Запрос возвращает код ответа 500, и содержит "Internal Server Error" в ответе')
    def test_create_order_with_invalid_hash(self):
        payload = {"ingredients": ["60d3b41abdooob0026a733c6"]}
        response = requests.post(f'{Data.URL}/api/orders',
                                 headers={"Authorization": TestCreateOrder.accessToken},
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
    def test_create_order_wo_ingredients(self, body):
        payload = body
        response = requests.post(f'{Data.URL}/api/orders',
                                 headers={"Authorization": TestCreateOrder.accessToken},
                                 data=payload)
        format_response = response.json()

        assert (response.status_code == 400 and format_response == Data.RESPONSE_CREATE_ORDER_NEGATIVE)

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Data.URL}/api/auth/user',
                        headers={"Authorization": TestCreateOrder.accessToken})
