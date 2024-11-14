# Заголовки указывающие, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Данные для создания пользователя
user_body = {
    "firstName": "Анастасия",
    "phone": "+79995553322",
    "address": "город Москва, ул. Пушкина, дом Колотушкина, 88"
}

# Данные для создания набора продуктов для существующего пользователя
headers_for_create_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 56a3fbf8-0bbf-41aa-ae80-b84032549f2a"
}

# Данные об имени набора продуктов
kit_body = {
"name": "Aa"
}

