#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from pytils import dt

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


# действие ru_strftime аналогично оригинальному strftime
# только в %a, %A, %b и %B вместо английских названий будут русские

d = datetime.date(2006, 9, 15)

# оригинал
print_(d.strftime("%d.%m.%Y (%a)"))
# -> 15.09.2006 (Fri)

# теперь на русском
# (единственно, что нужно формат строки передавать в unicode
# в то время, как в оригинальном strftime это обязательно str)
print_(dt.ru_strftime(u"%d.%m.%Y (%a)", d))
# -> 15.09.2006 (пт)

# %A дает полное название дня недели
print_(dt.ru_strftime(u"%d.%m.%Y (%A)", d))
# -> 15.09.2006 (пятница)

# %B -- название месяца
print_(dt.ru_strftime(u"%d %B %Y", d))
# -> 15 сентябрь 2006

# ru_strftime умеет правильно склонять месяц (опция inflected)
print_(dt.ru_strftime(u"%d %B %Y", d, inflected=True))
# -> 15 сентября 2006

# ... и день (опция inflected_day)
print_(dt.ru_strftime(u"%d.%m.%Y, в %A", d, inflected_day=True))
# -> 15.09.2006, в пятницу

# ... и добавлять правильный предлог (опция preposition)
print_(dt.ru_strftime(u"%d.%m.%Y, %A", d, preposition=True))
# -> 15.09.2006, в пятницу

# второй параметр можно не передавать, будет использована текущая дата
print_(dt.ru_strftime(u"%d %B %Y", inflected=True))
# ->> 1 декабря 2013