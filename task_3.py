"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
words = 'attribute', 'класс', 'функция', 'type'

for i in words:
    try:
        bword = bytes(i, 'utf-8')
        print(f"{i} can be represented as bytes: {bword}")
    except:
        print(f"{i} cannot be represented as bytes")