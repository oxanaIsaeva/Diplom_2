# Diplom_2

test_create_user.py

TestCreateUser - тесты на проверку создания пользователя
test_create_user_positive - Проверка создания уникального пользователя
test_create_user_duplicate - Проверка создания пользователя, который уже зарегистрирован
test_create_user_negative - Проверка создания пользователя без одного из обязательных полей

test_user_login.py

TestUserLogin - тесты на проверку логина пользователя
test_user_login_positive - Проверка логина под существующим пользователем
test_user_login_negative - Проверка логина с неверным логином и паролем

test_change_user_data.py

TestChangeUserData - тесты на проверку изменения данных пользователя
test_change_user_email - Проверка изменения электронной почты пользователя с авторизацией
test_change_user_name - Проверка изменения имени пользователя с авторизацией
test_change_user_password - Проверка изменения пароля пользователя с авторизацией
test_change_user_data_negative = Проверка изменения данных пользователя без авторизации
test_change_user_email_negative - Проверка изменения электронной почты пользователя на почту, которая уже используется

test_create_order.py

TestCreateOrder - тесты на проверку создания заказа
test_create_order_with_authorization - Проверка создания заказа с авторизацией
test_create_order_wo_authorization - Проверка создания заказа без авторизации
test_create_order_with_invalid_hash - Проверка создания заказа с невалидным хешем ингредиента
test_create_order_wo_ingredients - Проверка создания заказа без ингредиентов

test_get_orders.py

TestGetOrder - тесты на проверку получения заказов конкретного пользователя
test_create_order_with_authorization - Проверка получения заказов пользователя с авторизацией
test_create_order_wo_authorization - Проверка получения заказов пользователя без авторизацией


