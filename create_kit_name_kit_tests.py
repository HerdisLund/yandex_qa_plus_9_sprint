import sender_stand_request # Импорт модуля с запросами
import data # Импорт модуля с данными

# Функция замены значения в параметре name
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy() # Копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body["name"] = kit_name # Изменение значения в поле name
    return current_kit_body # Возвращается новый словарь с нужным значением name

# Функция для позитивной проверки
def positive_assert(kit_name):
    kit_body_positive = get_kit_body(kit_name)  # В переменную kit_body сохраняется обновлённое тело запроса
    kit_response_positive = sender_stand_request.create_kit_name(kit_body_positive)

    assert kit_response_positive.json()["name"] == kit_name # Проверка, что имя набора продуктов соответствует ожидаемому
    assert kit_response_positive.status_code == 201 # Проверка, что код ответа равен 201

# Функция для негативной проверки
def negative_assert(kit_name):
    kit_body_negative = get_kit_body(kit_name) # В переменную kit_body_negative сохраняется обновлённое тело запроса
    kit_response_negative = sender_stand_request.create_kit_name(kit_body_negative) # В переменную kit_response_negative сохраняется результат запроса

    assert kit_response_negative.status_code == 400 # Проверка, что код ответа равен 400
    assert kit_response_negative.json()["code"] == 400 # Проверка, что в теле ответа атрибут "code" равен 400

# Тест 1. Успешное создание набора продуктов для существующего пользователя [Параметр name = 1 символ]
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора продуктов для существующего пользователя [Параметр name = 511 символов]
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Ошибка при создании набора продуктов для существующего пользователя [Параметр name = пустой ввод]
def test_create_kit_empty_input_in_kit_name_get_error_response():
    negative_assert("")

# Тест 4. Ошибка при создании набора продуктов для существующего пользователя [Параметр name = 512 символов]
def test_create_kit_512_letter_in_kit_name_get_error_response():
        negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Успешное создание набора продуктов для существующего пользователя [Параметр name англ буквы = "QWErty"]
def test_create_kit_english_letter_in_kit_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора продуктов для существующего пользователя [Параметр name русс буквы = "Мария"]
def test_create_kit_russian_letter_in_kit_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора продуктов для существующего пользователя [Параметр name спец символы  = ""№%@",]
def test_create_kit_symbol_in_kit_name_get_success_response():
    positive_assert('"№%@",')

# Тест 8. Успешное создание набора продуктов для существующего пользователя [Параметр name содержит пробелы = " Человек и КО "]
def test_create_kit_name_with_spaces_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Успешное создание набора продуктов для существующего пользователя [Параметр name цифры строкой = 123]
def test_create_kit_str_numbers_in_kit_name_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка при создании набора продуктов для существующего пользователя [Параметр name не передан]
def test_create_kit_dont_get_kit_name_get_error_response():
    current_kit_body_without_name = data.kit_body.copy() # Копирую словарь с телом kit_body
    current_kit_body_without_name.pop("name") # Удаляю параметр name
    negative_assert(current_kit_body_without_name) # Проверяю ответ

# Тест 11. Ошибка при создании набора продуктов для существующего пользователя [Параметр name целое число]
def test_create_kit_int_numbers_in_kit_name_get_error_response():
    negative_assert(123)















