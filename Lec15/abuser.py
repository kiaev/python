"""
Подгрузка модуля funcs.py с разделенной областью именования
При импортировании модуля - интерпретатор выполняет целиком
импортируемый модуль, и только после этого возвращает управление
к abuser.py

Если нам лень писать много букав
"""
import funcs as f


def add(a,b):
    return a + b**2

print("My add(2,3):", add(2,3))

print("From funcs add(2,3):", f.add(2,3))
print("Temp:", f.TEMPERATURE)
