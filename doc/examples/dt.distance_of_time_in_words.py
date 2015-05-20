#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import time
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

# поддерживаются оба модуля работы со временем:
# time
current_time = time.time()
in_past = current_time - 100000
in_future = current_time + 100000
# и datetime.datetime
dt_current_time = datetime.datetime.now()
dt_in_past = dt_current_time - datetime.timedelta(0, 100000)
dt_in_future = dt_current_time + datetime.timedelta(0, 100000)

#
# У distance_of_time_in_words три параметра:
# 1) from_time, время от которого считать
# 2) accuracy, точность, по умолчанию -- 1
# 3) to_time, до которого времени считать, по умолчанию - сейчас
#

# если to_time не передано, считается от "сейчас",
# и тогда -1 день -> "вчера", а +1 день -> "завтра"
print_(dt.distance_of_time_in_words(in_past))
#-> вчера
print_(dt.distance_of_time_in_words(dt_in_future))
#-> завтра


# а вот если передано to_time, то нельзя говорить "вчера",
# потому что to_time не обязательно "сейчас",
# поэтому -1 день -> "1 день назад"
print_(dt.distance_of_time_in_words(in_past, to_time=current_time))
#-> 1 день назад

# увеличение точности отражается на результате
print_(dt.distance_of_time_in_words(in_past, accuracy=2))
#-> 1 день 3 часа назад
print_(dt.distance_of_time_in_words(in_past, accuracy=3))
#-> 1 день 3 часа 46 минут назад

# аналогично и с будущим временем:
print_(dt.distance_of_time_in_words(in_future))
#-> завтра
print_(dt.distance_of_time_in_words(in_future, to_time=current_time))
#-> через 1 день
print_(dt.distance_of_time_in_words(in_future, accuracy=2))
#-> через 1 день 3 часа
print_(dt.distance_of_time_in_words(in_future, accuracy=3))
#-> через 1 день 3 часа 46 минут
