import configuration # Импорт модуля с конфигурациями
import requests # Импорт библиотеки requests
import data # Импорт модуля с данными

# Функция создания нового пользователя
def post_new_user(body):
       return requests.post(configuration.BASE_URL + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Функция получения аутентификатора для пользователя
def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken") # Извлекаем значение по ключу "authToken", выданный сервером после успешной регистрации пользователя

# Функция создания нового набора продуктов для пользователя с полученным аутентификатором
def create_kit_name(body):
    headers_with_token = data.headers.copy()
    headers_with_token["Authorization"] = "Bearer " + get_new_user_token() # В копию заголовков добавляется новый ключ Authorization. В значение добавляется строка "Bearer " + добавляем сам токен, который был получен из функции get_new_user_token()
    return requests.post(configuration.BASE_URL + configuration.CREATE_KITS_PATH,
                         json=body,
                         headers=headers_with_token)