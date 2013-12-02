#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytils import translit

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

# простая траслитерация/детранслитерация
# обратите внимание на то, что при транслитерации вход - unicode,
# выход - str, а в детранслитерации -- наоборот
#

print_(translit.translify(u"Это тест и ничего более"))
#-> Eto test i nichego bolee

print_(translit.translify(u"Традиционно сложные для транслитерации буквы - подъезд, щука"))
#-> Traditsionno slozhnyie dlya transliteratsii bukvyi - pod`ezd, schuka

# и теперь пытаемся вернуть назад... (понятно, что Э и Е получаются одинаково)
print_(translit.detranslify("Eto test i nichego bolee"))
#-> Ето тест и ничего более

print_(translit.detranslify("Traditsionno slozhnyie dlya transliteratsii bukvyi - pod`ezd, schuka"))
#-> Традиционно сложные для транслитерации буквы – подЪезд, щука


# и пригодные для url и названий каталогов/файлов транслиты
# dirify и slugify -- синонимы, действия абсолютно идентичны
print_(translit.slugify(u"Традиционно сложные для транслитерации буквы - подъезд, щука"))
#-> traditsionno-slozhnyie-dlya-transliteratsii-bukvyi-podezd-schuka

# обратного преобразования, понятно, нет :)
