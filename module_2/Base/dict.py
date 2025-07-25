# my_dict = {
#     'x':'y',
#     'c':'z'
# }
#
# print(my_dict.get("name"))         # Вывод: Alice
# print(my_dict.get("country", "USA"))  # Вывод: USA (значение по умолчанию)

# print(my_dict.get("unknown"))  # Вывод: None
# print(my_dict["unknown"])      # Ошибка: KeyError

# my_dict = {"name": "Alice", "age": 25}
#
# # Добавление нового элемента
# my_dict["city"] = "New York"
# print(my_dict)  # Вывод: {'name': 'Alice', 'age': 25, 'city': 'New York'}

'''### Задание 1

1. Создай словарь со своими персональными данными (допустим анкету)
который будет содержать имя, возраст, имейл.
2. Попробуй скопировать его методом copy() в другую переменную
3. При помощи assert сравни оба словаря и проверь результат работы программы

### Задание 2

1. В созданном раннее словаре добавь новую пару ключ-значение - свой номер телефона
2. Выведи результат полученный номер телефона в консоль при помощи `print()`
3. после этого перезапиши значение этого элемента сделав его отфильтрованным 🍻 (добавь символы `*` что бы персональные данные были скрыты.
Например: 797*****33

### Задание 3

1. Создать второй словарь, который будет вложенным, где будет находиться информация о твоем месте жительства (можно фейково)
Например:

```python
residence = {
    "residence": {
        "country": "Thailand",
        "city": "Phuket",
        "district": "Thalang"
    }
}
```

1. Объедини списки, добавив в анкету о себе информацию о месте жительства
2. После этого выведи город (или другой созданный элемент) из вложенного списка который мы добавили к первому'''


# my_dict = dict()
# my_dict = {
#     'name': 'M',
#     'age': 48,
#     'email': 'example@example.com'
# }
# my_new_dict = my_dict.copy()
# print(my_new_dict)
# assert my_dict == my_new_dict, 'словари не равны'

# my_dict = dict()
# my_dict = {
#     'name': 'M',
#     'age': 48,
#     'email': 'example@example.com'
# }
#
# my_dict['phone'] = '79138818888'
# print(my_dict)
# my_dict['phone'] = '7913*****88'
# print(my_dict)
# print(len(my_dict['phone']))

# residence = {
#     "residence": {
#         "country": "Thailand",
#         "city": "Phuket",
#         "district": "Thalang"
#     }
# }
#
# my_dict = dict()
# my_dict = {
#     'name': 'M',
#     'age': 48,
#     'email': 'example@example.com',
#     'phone':'79138818888'
# }
#
# my_new_dict = my_dict | residence
# print(my_new_dict)
# print(my_new_dict['residence']['district'])