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


# sum_string объединяет в себе choose_plural и in_words
# т.е. передаются и количество, и варианты названия объекта
# а на выходе получаем количество объектов в правильной форме

# параметры:
# 1) amount, количество (только целое)
# 2) gender, пол (1=мужской, 2=женский, 3=средний)
# 3) items, варианты названий объекта (необязательно),
#    правила аналогичны таковым у choose_plural

print_(numeral.sum_string(3, numeral.MALE, (u"носок", u"носка", u"носков")))
#-> три носка

print_(numeral.sum_string(5, numeral.FEMALE, (u"коробка", u"коробки", u"коробок")))
#-> пять коробок

print_(numeral.sum_string(21, numeral.NEUTER, (u"очко", u"очка", u"очков")))
#-> двадцать одно очко

# если варианты не указывать, то действие функции аналогично дейтсвию in_words
print_(numeral.sum_string(21, gender=numeral.NEUTER))
#-> двадцать одно


