import pytest
import requests

from data import Data


# Фикстура создания/удаления пользователя
@pytest.fixture
def create_new_user():
    payload = Data.CREATE_USER
    response = requests.post(f'{Data.URL}/api/auth/register', data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(f'{Data.URL}/api/auth/user',
                    headers={"Authorization": token})
