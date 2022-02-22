#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import numeral

# rubles служит для формирования строк с деньгами

print(numeral.rubles(10))
#-> десять рублей

# если нужно, то даже 0 копеек можно записать словами
print(numeral.rubles(10, zero_for_kopeck=True))
#-> десять рублей ноль копеек

print(numeral.rubles(2.35))
#-> два рубля тридцать пять копеек

# в случае чего, копейки округляются
print(numeral.rubles(3.95754))
#-> три рубля девяносто шесть копеек
