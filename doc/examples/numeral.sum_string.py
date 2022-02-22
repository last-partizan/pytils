#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import numeral

# sum_string объединяет в себе choose_plural и in_words
# т.е. передаются и количество, и варианты названия объекта
# а на выходе получаем количество объектов в правильной форме

# параметры:
# 1) amount, количество (только целое)
# 2) gender, пол (1=мужской, 2=женский, 3=средний)
# 3) items, варианты названий объекта (необязательно),
#    правила аналогичны таковым у choose_plural

print(numeral.sum_string(3, numeral.MALE, ("носок", "носка", "носков")))
#-> три носка

print(numeral.sum_string(5, numeral.FEMALE, ("коробка", "коробки", "коробок")))
#-> пять коробок

print(numeral.sum_string(21, numeral.NEUTER, ("очко", "очка", "очков")))
#-> двадцать одно очко

# если варианты не указывать, то действие функции аналогично дейтсвию in_words
print(numeral.sum_string(21, gender=numeral.NEUTER))
#-> двадцать одно


