import allure
import requests
from data import Data
from conftest import create_new_user


class TestGetOrder:

    @allure.title('Проверка получения заказов пользователя с авторизацией')
    @allure.description('Запрос возвращает код ответа 200, и содержит "success" и "orders" в ответе')
    def test_create_order_with_authorization(self, create_new_user):
        token = create_new_user[1].json()["accessToken"]
        requests.post(f'{Data.URL}/api/orders',
                      headers={"Authorization": token},
                      data=Data.INGREDIENTS)
        response = requests.get(f'{Data.URL}/api/orders',
                                headers={"Authorization": token})
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
