"""
Самая большая проблема!!! Неоднозначность сигнатуры приводит к использованию фукнции не по назначению.
"""
def add(a , b):
    return a + b 

"""
Аннотация - это не ограничение типа. Это подсказка другим разработчикам, что вы бы очень хотели
чтобы параметры были такого типа.
"""
def add_new(a:int, b:int):
    """
    Супер-пупер документация
    для супер-пупер функции
    Принимает на вход 2 параметра (желательно целочисленных)
    Возвращает результат сложения (арифметического)
    """
    return a + b 

print(add_new(10, 20))
print(add_new("File", "Input"))
print(add_new("10", "20"))
print(add_new(True, False))




