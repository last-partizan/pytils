#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import numeral

def print_(s):
    # pytils всегда возвращает юникод (строка в Py3.x)
    # обычно это ОК выводить юникод в терминал
    # но если это неинтерактивный вывод
    # (например, использования модуля subprocess)
    # то для Py2.x нужно использовать перекодировку в utf-8
    from pytils.third import six
    if six.PY3:
        out = s
    else:
        out = s.encode('UTF-8')
    print(out)


# in_words нужен для представления цифр словами

print_(numeral.in_words(12))
#-> двенадцать

# вторым параметром можно задать пол:
# мужской=numeral.MALE, женский=numeral.FEMALE, срелний=numeral.NEUTER (по умолчанию -- мужской)
print_(numeral.in_words(21))
#-> двадцать один

# можно передавать неименованным параметром:
print_(numeral.in_words(21, numeral.FEMALE))
#-> двадцать одна

# можно именованным
print_(numeral.in_words(21, gender=numeral.FEMALE))
#-> двадцать одна
print_(numeral.in_words(21, gender=numeral.NEUTER))
#-> двадцать одно

# можно и дробные
print_(numeral.in_words(12.5))
#-> двенадцать целых пять десятых

# причем "пишутся" только значимые цифры
print_(numeral.in_words(5.30000))
#-> пять целых три десятых
