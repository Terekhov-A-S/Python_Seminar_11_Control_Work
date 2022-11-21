"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции

"""
# ############### Так стало: ###############

import binascii

text = [b'class', b'function', b'method']

for s in text:
    print(type(s), binascii.hexlify(s), len(s))


# ############### Так было: ###############

# p1 = b'class'
# p2 = b'function'
# p3 = b'method'
# print(type(p1), type(p2), type(p3))
# print(p1, p2, p3)
# print(len(p1), len(p2), len(p3))
