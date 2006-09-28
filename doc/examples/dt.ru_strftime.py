#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import pytils

# действие ru_strftime аналогично оригинальному strftime
# только в %a, %A, %b и %B вместо английских названий будут русские

d = datetime.date(2006, 9, 15)

# оригинал
print d.strftime("%d.%m.%Y (%a)")
# -> 15.09.2006 (Fri)

# теперь на русском
# (единственно, что нужно формат строки передавать в unicode
# в то время, как в оригинальном strftime это обязательно str)
print pytils.dt.ru_strftime(u"%d.%m.%Y (%a)", d)
# -> 15.09.2006 (пт)

# %A дает полное название дня недели
print pytils.dt.ru_strftime(u"%d.%m.%Y (%A)", d)
# -> 15.09.2006 (пятница)

# %B -- название месяца
print pytils.dt.ru_strftime(u"%d %B %Y", d)
# -> 15 сентябрь 2006

# ru_strftime умеет правильно склонять месяц (опция inflected)
print pytils.dt.ru_strftime(u"%d %B %Y", d, inflected=True)
# -> 15 сентября 2006

# ... и день (опция inflected_day)
print pytils.dt.ru_strftime(u"%d.%m.%Y, в %A", d, inflected_day=True)

# второй параметр можно не передавать, будет использована текущая дата
print pytils.dt.ru_strftime(u"%d %B %Y", inflected=True)
