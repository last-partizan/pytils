#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from pytils import dt

# действие ru_strftime аналогично оригинальному strftime
# только в %a, %A, %b и %B вместо английских названий будут русские

d = datetime.date(2006, 9, 15)

# оригинал
print(d.strftime("%d.%m.%Y (%a)"))
# -> 15.09.2006 (Fri)

# теперь на русском
# (единственно, что нужно формат строки передавать в unicode
# в то время, как в оригинальном strftime это обязательно str)
print(dt.ru_strftime("%d.%m.%Y (%a)", d))
# -> 15.09.2006 (пт)

# %A дает полное название дня недели
print(dt.ru_strftime("%d.%m.%Y (%A)", d))
# -> 15.09.2006 (пятница)

# %B -- название месяца
print(dt.ru_strftime("%d %B %Y", d))
# -> 15 сентябрь 2006

# ru_strftime умеет правильно склонять месяц (опция inflected)
print(dt.ru_strftime("%d %B %Y", d, inflected=True))
# -> 15 сентября 2006

# ... и день (опция inflected_day)
print(dt.ru_strftime("%d.%m.%Y, в %A", d, inflected_day=True))
# -> 15.09.2006, в пятницу

# ... и добавлять правильный предлог (опция preposition)
print(dt.ru_strftime("%d.%m.%Y, %A", d, preposition=True))
# -> 15.09.2006, в пятницу

# второй параметр можно не передавать, будет использована текущая дата
print(dt.ru_strftime("%d %B %Y", inflected=True))
# ->> 1 декабря 2013