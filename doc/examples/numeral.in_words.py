#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import numeral

# in_words нужен для представления цифр словами

print(numeral.in_words(12))
#-> двенадцать

# вторым параметром можно задать пол:
# мужской=numeral.MALE, женский=numeral.FEMALE, срелний=numeral.NEUTER (по умолчанию -- мужской)
print(numeral.in_words(21))
#-> двадцать один

# можно передавать неименованным параметром:
print(numeral.in_words(21, numeral.FEMALE))
#-> двадцать одна

# можно именованным
print(numeral.in_words(21, gender=numeral.FEMALE))
#-> двадцать одна
print(numeral.in_words(21, gender=numeral.NEUTER))
#-> двадцать одно

# можно и дробные
print(numeral.in_words(12.5))
#-> двенадцать целых пять десятых

# причем "пишутся" только значимые цифры
print(numeral.in_words(5.30000))
#-> пять целых три десятых
