'''if-else (простые типы данных)
<aside> 🍄
1. Написать конструкцию if-else, которая будет проверять число в переменной - четное оно или нет, выводит сообщение на экран
2. Задаем 2 переменные - первая это кол-во товара, вторая - сумма за 1 единицу.
Задача - вывести итоговую сумму заказа Если сумма больше 5000, скидка 10%. Если больше 10000, скидка 20%
Вывести надо именно итоговую сумму!
3. Написать проверку пароля. В переменной должен лежать пароль “qwerty123”.
Если пароль совпадает - вывести “доступ разрешен” Если пароль пустой - вывести что нужен пароль </aside>
'''

# x = 15
# if x%2 == 0:
#     print(f'Число {x} - четное')
# else:
#     print(f'Число {x} - НЕ четное')

# try:
#     item = 10
#     price = 'a'
#     total = item*price
#     if total <= 5000:
#         print(total, 'sale 0%')
#     elif 5000 < total <=10000:
#         print(total*0.9, 'sale 10%')
#     elif total>10000:
#         print(total*0.8, 'sale 20%')
#     else:
#         print('WTF?')
# except (NameError, TypeError, ValueError):
#     print('WTF bro?')

# try:
#     password = 'qwerty123'
#     user_pass = input('Введи пароль: ')
#     if password == user_pass:
#         print('Доступ разрешен')
#     elif user_pass == '':
#         print('Пустой пароль')
#     else:
#         print('Доступ запрещен')
# except(NameError, TypeError, ValueError):
#     print('WTF bro?')
