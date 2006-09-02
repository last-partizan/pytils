# -*- coding: utf-8 -*-
# License: GNU GPL2 
# Author: Pythy <the.pythy@gmail.com>
"""
Simple processing for russian strings
"""

__id__ = "$Id$"
__url__ = "$URL$"
__all__ = ["numeral", "dt", "translit", "test"]

# версия PyTils
VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_TINY = 0

VERSION = "%d.%d.%d" % (VERSION_MAJOR, VERSION_MINOR, VERSION_TINY)

REL_DATE = '20060902'

def __get_svn_date_from_id(id_string):
    if id_string.replace('$', '') == "Id":
        return REL_DATE
    else:
        return id_string.split()[3].replace('-', '')


__module_dates = [__get_svn_date_from_id(__id__), ]

# импорт модулей
for __module_name in __all__:
    __imported_module = __import__("pytils."+__module_name, globals(), locals(), ["pytils"])
    __module_dates.append(__get_svn_date_from_id(__imported_module.__id__))

SVN_DATE = max(__module_dates)

# если взяли с svn, то версия будет
# X.Y.Z-svnYYYYMMDD, где X.Y.Z - номер оригинальной версии,
# а YYYYMMDD - дата последнего изменения в модулях
# единственная сложность остается, если взяли не через svn,
# а через webdav, в этом случае Id не проставляется и версия
# будет оригинальной. Это можно обойти, скажем, учитывая дату
# изменения файлов, но я пока не вижу в этом смысла.
if SVN_DATE > REL_DATE:
    VERSION = "%s-svn%s" % (VERSION, SVN_DATE)


