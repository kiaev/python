"""
Управляющая конструкция 1.
Условный оператор.
"""


# if expression:
#     body 

# Что можно использовать в кач-ве expression?
# Основаные на числовых сравнениях
print(">", 10  > 2) # <
print(">=", 10.0 >= 10) # <=
print("==", 0.0 == 0)
print("!=", 5 != 4)

print((10 > 2) and (10 <= 15))

# Содержание строки
message = "Hello"
# Для того, чтобы проверить входит ли ПОДСТРОКА 'e' в строку 'Hello'
print('e' in message)
# Для того, чтобы проверить входит ли ПОДСТРОКА 'Hell' в строку 'Hello'
print("Hell" in message)


# Условие на ждину
print(len(message) >= 5)

