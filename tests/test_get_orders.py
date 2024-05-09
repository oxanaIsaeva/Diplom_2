import allure
import requests
from data import Data


class TestGetOrder:
    accessToken = ''
    ingredients = []

    @classmethod
    def setup_class(cls):
        payload = Data.CREATE_USER
        response = requests.post(f'{Data.URL}/api/auth/register', data=payload)
        format_response = response.json()
        TestGetOrder.accessToken = format_response["accessToken"]

        response_ingredients = requests.get(f'{Data.URL}/api/ingredients')
        format_response_ingredients = response_ingredients.json()
        list_of_ingredients = format_response_ingredients["data"]
        ingredient_1 = list_of_ingredients[1]
        ingredient_2 = list_of_ingredients[4]
        TestGetOrder.ingredients.append(ingredient_1["_id"])
        TestGetOrder.ingredients.append(ingredient_2["_id"])

        payload_ingredients = {"ingredients": TestGetOrder.ingredients}
        requests.post(f'{Data.URL}/api/orders',
                      headers={"Authorization": TestGetOrder.accessToken},
                      data=payload_ingredients)

    @allure.title('Проверка получения заказов пользователя с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "orders" в ответе')
    def test_create_order_with_authorization(self):
        response = requests.get(f'{Data.URL}/api/orders',
                                headers={"Authorization": TestGetOrder.accessToken})
        format_response = response.json()

        assert (response.status_code == 200 and 'success' in format_response.keys() and
                'orders' in format_response.keys())

    @allure.title('Проверка получения заказов пользователя без авторизацией')
    @allure.description('Запрос возвращает код ответа 401 и ответ {"success": False, "message": "You should be '
                        'authorised"}')
    def test_create_order_wo_authorization(self):
        response = requests.get(f'{Data.URL}/api/orders')
        format_response = response.json()

        assert (response.status_code == 401 and format_response == Data.RESPONSE_GET_ORDER_NEGATIVE)

    @classmethod
    def teardown_class(cls):
        requests.delete(f'{Data.URL}/api/auth/user',
                        headers={"Authorization": TestGetOrder.accessToken})
