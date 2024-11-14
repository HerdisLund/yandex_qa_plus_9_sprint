import configuration # Импорт модуля с конфигурациями
import requests # Импорт библиотеки requests
import data # Импорт модуля с данными

# Функция создания нового пользователя
def post_new_user(body):
       return requests.post(configuration.BASE_URL + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body) # Выполнить функцию с использованием данных user_body

print(response.status_code) # Вывести код статуса
print(response.json()) # Вывести полученный ответ

# Функция создания нового набора продуктов для определенного пользователя
def create_kit_name(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_KITS_PATH,
                         json=body,
                         headers=data.headers_for_create_kit)
response = create_kit_name(data.kit_body) # Выполнить функцию с использованием данных kit_body

print(response.status_code) # Вывести код статуса
print(response.json()) # Вывести полученный ответ