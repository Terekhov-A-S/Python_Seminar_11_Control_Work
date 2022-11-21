"""
Задание 6.

Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться!

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО!!! в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb
для последующей переконвертации в нужную кодировку

НАРУШЕНИЕ обозначенных условий - задание не выполнено!!!
"""


import locale
import chardet


print(f'ОПРЕДЕЛЕНИЕ КОДИРОВКИ: {locale.getpreferredencoding()}', end='\n'
      f'ДЕКОДИНГ: ')

with open('test_file.txt', 'rb') as i:
    text = i.read()
    print(text)
    print(chardet.detect(text))

with open('test_file.txt', encoding='utf-8', errors='replace') as j:
    print(j.read())


# Так же вначале пытался изобразить иначе:
# text_file = open('test_file.txt', 'w', encoding='windows-1251')
# text_file.write('«сетевое программирование», «сокет», «декоратор»')
# text_file.close()
# print(type(text_file))

# with open('test_file.txt', 'rb') as txt_file:
#     context = txt_file.read()
#     result = chardet.detect(context)
#     encoding = result['encoding']
#     text_encode = context.decode(encoding)
#     with open('test_file.txt', 'w', encoding='utf-8') as txt_file:
#         txt_file.write(text_encode)

# with open('test_file.txt', 'r', encoding='utf-8') as txt_file:
#     text_encode = txt_file.read()

# print(text_encode)
