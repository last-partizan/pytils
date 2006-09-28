#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytils

# rubles служит для формирования строк с деньгами :)

print pytils.numeral.rubles(10)
#-> десять рублей

# если нужно, то даже 0 копеек можно записать словами
print pytils.numeral.rubles(10, zero_for_kopeck=True)
#-> десять рублей ноль копеек

print pytils.numeral.rubles(2.35)
#-> два рубля тридцать пять копеек

# в случае чего, копейки округляются
print pytils.numeral.rubles(3.95754)
#-> три рубля девяносто шесть копеек
