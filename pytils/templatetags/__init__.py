# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2008  Yury Yurevich
#
# http://www.pyobject.ru/pythy/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Pytils templatetags for Django web-framework
"""

import warnings
import django

from pytils import utils

def is_django_unicode_aware():
    if django.VERSION[:2] > (0, 96):
        return True
    else:
        return False

text_version = '.'.join(str(v) for v in django.VERSION if v is not None)
unicode_aware = is_django_unicode_aware()
if not unicode_aware:
    warnings.warn('Django %s is not unicode-aware, please upgrade your Django to unicode-branch' % text_version, DeprecationWarning)

# Если отладка, то показываем 'unknown+сообщение об ошибке'.
# Если отладка выключена, то можно чтобы при ошибках показывалось
# значение, переданное фильтру (PYTILS_SHOW_VALUES_ON_ERROR=True)
# либо пустая строка.
def init_defaults(debug, show_value):
    if debug:
        default_value = "unknown: %(error)s"
        default_uvalue = u"unknown: %(error)s"
    elif show_value:
        default_value = "%(value)s"
        default_uvalue = u"%(value)s"
    else:
        default_value = ""
        default_uvalue = u""
    return default_value, default_uvalue

def pseudo_unicode(stext, encoding, default_value=u''):
    """
    Return (unicode) stext if Django is unicode-aware,
    decode from encoding otherwise.
    
    It raises UnicodeDecodeError when such error occures
    and default_value is None. Otherwise (i.e. 
    default_value is not None), it return default_value.
    
    """
    if unicode_aware and isinstance(stext, unicode):
        utext = stext
    elif isinstance(stext, unicode):
        utext = stext
    else:
        try:
            utext = unicode(stext, encoding)
        except UnicodeDecodeError, err:
            if default_value is None:
                raise UnicodeDecodeError, err
            utext = default_value % {'error': err, 'value': u""}
    return utext


def pseudo_str(utext, encoding, default_value=''):
    """
    Return (unicode) utext if Django is unicode-aware,
    encode to encoding otherwise

    It raises UnicodeEncodeError when such error occures
    and default_value is None. Otherwise (i.e. 
    default_value is not None), it return default_value.
    """
    if unicode_aware and isinstance(utext, unicode):
        stext = utext
    else:
        try:
            stext = unicode(utext).encode(encoding)
        except (UnicodeEncodeError, UnicodeDecodeError), err:
            if default_value is None:
                raise UnicodeEncodeError, err
            stext = default_value % {'error': err, 'value': ""}
    return stext
