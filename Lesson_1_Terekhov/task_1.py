"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции

ВНИМАНИЕ!!: сдача задания
1) создать папку Lesson_1_Ivanov
2) в папку положить файлы task_1 - task_6 (а также txt-файл для последнего)
3) заархивировать папку! и сдать архив

Все другие варианты сдачи приму только один раз, потом буду ставить НЕ СДАНО

"""
# ############### Так стало: ###############

text = ['разработка', 'сокет', 'декоратор']

for s in text:
    print(type(s), s)

text_unicode = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]
print(text_unicode)

for s in text_unicode:
    print(type(s), s)


# ############### Так было: ###############

# s1 = 'разработка'
# s2 = 'сокет'
# s3 = 'декоратор'

# print(type(s1))
# print(type(s2))
# print(type(s3))
# print(s1, s2, s3)

# s1_u = u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
# s2_u = u'\u0441\u043e\u043a\u0435\u0442'
# s3_u = u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
# print(type(s1_u), type(s2_u), type(s3_u))
# print(s1_u, s2_u, s3_u)
