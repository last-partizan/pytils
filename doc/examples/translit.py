#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import translit

# простая траслитерация/детранслитерация
# обратите внимание на то, что при транслитерации вход - unicode,
# выход - str, а в детранслитерации -- наоборот
#

print(translit.translify("Это тест и ничего более"))
#-> Eto test i nichego bolee

print(translit.translify("Традиционно сложные для транслитерации буквы - подъезд, щука"))
#-> Traditsionno slozhnyie dlya transliteratsii bukvyi - pod`ezd, schuka

# и теперь пытаемся вернуть назад... (понятно, что Э и Е получаются одинаково)
print(translit.detranslify("Eto test i nichego bolee"))
#-> Ето тест и ничего более

print(translit.detranslify("Traditsionno slozhnyie dlya transliteratsii bukvyi - pod`ezd, schuka"))
#-> Традиционно сложные для транслитерации буквы – подЪезд, щука


# и пригодные для url и названий каталогов/файлов транслиты
# dirify и slugify -- синонимы, действия абсолютно идентичны
print(translit.slugify("Традиционно сложные для транслитерации буквы - подъезд, щука"))
#-> traditsionno-slozhnyie-dlya-transliteratsii-bukvyi-podezd-schuka

# обратного преобразования, понятно, нет :)
