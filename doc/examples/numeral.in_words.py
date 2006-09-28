#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytils

# in_words нужен для представления цифр словами

print pytils.numeral.in_words(12)
#-> двенадцать

# вторым параметром можно задать пол:
# мужской=1, женский=2, срелний=3 (по умолчанию -- мужской)
print pytils.numeral.in_words(21)
#-> двадцать один
print pytils.numeral.in_words(21, gender=2)
#-> двадцать одна
print pytils.numeral.in_words(21, gender=3)
#-> двадцать одно

# можно и дробные
print pytils.numeral.in_words(12.5)
#-> двенадцать целых пять десятых

# причем "пишутся" только значимые цифры
print pytils.numeral.in_words(5.30000)
#-> пять целых три десятых
