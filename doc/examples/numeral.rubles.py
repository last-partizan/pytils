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


# rubles служит для формирования строк с деньгами

print_(numeral.rubles(10))
#-> десять рублей

# если нужно, то даже 0 копеек можно записать словами
print_(numeral.rubles(10, zero_for_kopeck=True))
#-> десять рублей ноль копеек

print_(numeral.rubles(2.35))
#-> два рубля тридцать пять копеек

# в случае чего, копейки округляются
print_(numeral.rubles(3.95754))
#-> три рубля девяносто шесть копеек
