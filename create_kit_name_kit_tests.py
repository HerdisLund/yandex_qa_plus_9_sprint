import sender_stand_request # Импорт модуля с запросами
import data # Импорт модуля с данными

# Эта функция меняет значение в параметре name
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy() # Копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body["name"] = kit_name # Изменение значения в поле name
    return current_kit_body # Возвращается новый словарь с нужным значением name

# Тест 1. Успешное создание набора продуктов для существующего пользователя [Параметр name = 1 символ]
def test_create_kit_1_letter_in_kit_name_get_success_response():
    kit_body = get_kit_body("a") # В переменную kit_body сохраняется обновленное тело запроса с именем "а"
    kit_response = sender_stand_request.create_kit_name(kit_body) # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201 # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == "a" # Проверяется, что заполнено name со значением "а"

# Тест 2. Успешное создание набора продуктов для существующего пользователя [Параметр name = 511 символов]
def test_create_kit_511_letters_in_kit_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC") # В переменную kit_body сохраняется обновленное тело запроса с именем из 511 символов
    kit_response = sender_stand_request.create_kit_name(kit_body) # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201 # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC" # Проверяется, что заполнено name со значением из 511 символов

# Эта функция для негативной проверки
def negative_assert_symbol(kit_name):
    kit_body = get_kit_body(kit_name) # В переменную kit_body сохраняется обновлённое тело запроса
    response = sender_stand_request.create_kit_name(kit_body) # В переменную response сохраняется результат запроса

    assert response.status_code == 400 # Проверка, что код ответа равен 400
    assert response.json()["code"] == 400 # Проверка, что в теле ответа атрибут "code" равен 400

# Тест 3. Ошибка при создании набора продуктов для существующего пользователя [Параметр name = пустой ввод]
def test_create_kit_empty_input_in_kit_name_get_error_response():
    negative_assert_symbol("")

# Тест 4. Ошибка при создании набора продуктов для существующего пользователя [Параметр name = 512 символов]
def test_create_kit_512_letter_in_kit_name_get_error_response():
        negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Успешное создание набора продуктов для существующего пользователя [Параметр name англ буквы = "QWErty"]
def test_create_kit_english_letter_in_kit_name_get_success_response():
    kit_body = get_kit_body("QWErty")  # В переменную kit_body сохраняется обновленное тело запроса с именем "QWErty"
    kit_response = sender_stand_request.create_kit_name(
        kit_body)  # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201  # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == "QWErty"  # Проверяется, что заполнено name со значением "QWErty"

# Тест 6. Успешное создание набора продуктов для существующего пользователя [Параметр name русс буквы = "Мария"]
def test_create_kit_russian_letter_in_kit_name_get_success_response():
    kit_body = get_kit_body("Мария")  # В переменную kit_body сохраняется обновленное тело запроса с именем "Мария"
    kit_response = sender_stand_request.create_kit_name(
        kit_body)  # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201  # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == "Мария"  # Проверяется, что заполнено name со значением "Мария"

# Тест 7. Успешное создание набора продуктов для существующего пользователя [Параметр name спец символы  = ""№%@",]
def test_create_kit_symbol_in_kit_name_get_success_response():
    kit_body = get_kit_body('"№%@",')  # В переменную kit_body сохраняется обновленное тело запроса с именем "№%@",
    kit_response = sender_stand_request.create_kit_name(
        kit_body)  # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201  # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == '"№%@",' # Проверяется, что заполнено name со значением "№%@",

# Тест 8. Успешное создание набора продуктов для существующего пользователя [Параметр name содержит пробелы = " Человек и КО "]
def test_create_kit_name_with_spaces_get_success_response():
    kit_body = get_kit_body(" Человек и КО ")  # В переменную kit_body сохраняется обновленное тело запроса с именем " Человек и КО "
    kit_response = sender_stand_request.create_kit_name(
        kit_body)  # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201  # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == " Человек и КО "  # Проверяется, что заполнено name со значением " Человек и КО "

# Тест 9. Успешное создание набора продуктов для существующего пользователя [Параметр name цифры строкой = 123]
def test_create_kit_str_numbers_in_kit_name_get_success_response():
    kit_body = get_kit_body("123")  # В переменную kit_body сохраняется обновленное тело запроса с именем 123
    kit_response = sender_stand_request.create_kit_name(
        kit_body)  # В переменную kit_response сохраняется результат запроса на создание пользователя

    assert kit_response.status_code == 201  # Проверяется, что код ответа равен 201
    assert kit_response.json()["name"] == "123"  # Проверяется, что заполнено name со значением 123

# Тест 10. Ошибка при создании набора продуктов для существующего пользователя [Параметр name не передан]
def test_create_kit_dont_get_kit_name_get_error_response():
        negative_assert_symbol()

# Тест 11. Ошибка при создании набора продуктов для существующего пользователя [Параметр name целое число]
def test_create_kit_int_numbers_in_kit_name_get_error_response():
    negative_assert_symbol(123)















