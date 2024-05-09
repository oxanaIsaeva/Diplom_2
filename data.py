import random


class Data:
    URL = 'https://stellarburgers.nomoreparties.site'

    number = random.randint(111, 999)

    CREATE_USER = {
        "email": f"test-Oxana{number}@yandex.ru",
        "password": "12345",
        "name": f"Oxana{number}"
    }

    CREATE_USER_DUPLICATE = {
        "email": "test-Oxana1@yandex.ru",
        "password": "12345",
        "name": "Oxana1"
    }

    LOGIN_USER = {
        "email": "test-Oxana1@yandex.ru",
        "password": "12345"
    }

    USER_CHANGE_EMAIL = {
        "email": f"test-ohhOxana{number}@yandex.ru"
    }

    USER_CHANGE_NAME = {
        "name": f"ohhOxana{number}"
    }

    USER_CHANGE_PASSWORD = {
        "password": f"12345{number}"
    }

    USER_CHANGE_EMAIL_NEGATIVE = {
        "email": "test-Oxana1@yandex.ru"
    }

    RESPONSE_DUPLICATE_USER = {'success': False, 'message': 'User already exists'}

    RESPONSE_CREATE_USER_NEGATIVE = {'success': False, 'message': 'Email, password and name are required fields'}

    RESPONSE_USER_LOGIN_NEGATIVE = {"success": False, "message": "email or password are incorrect"}

    RESPONSE_UPDATE_USER_DATA_NEGATIVE = {"success": False, "message": "You should be authorised"}

    RESPONSE_UPDATE_USER_EMAIL_NEGATIVE = {"success": False, "message": "User with such email already exists"}

    RESPONSE_CREATE_ORDER_NEGATIVE = {"success": False, "message": "Ingredient ids must be provided"}

    RESPONSE_GET_ORDER_NEGATIVE = {"success": False, "message": "You should be authorised"}
