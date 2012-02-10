# -*- coding: utf-8 -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2009  Yury Yurevich
#
# http://pyobject.ru/pythy/projects/pytils/
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

from __future__ import print_function, absolute_import, division, unicode_literals
import warnings
import six
import django

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
        default_uvalue = "unknown: %(error)s"
    elif show_value:
        default_value = "%(value)s"
        default_uvalue = "%(value)s"
    else:
        default_value = ""
        default_uvalue = ""
    return default_value, default_uvalue

def pseudo_unicode(stext, encoding, default_value=''):
    """
    Return (unicode) stext if Django is unicode-aware,
    decode from encoding otherwise.

    It raises UnicodeDecodeError when such error occures
    and default_value is None. Otherwise (i.e.
    default_value is not None), it return default_value.

    """
    if unicode_aware and isinstance(stext, six.text_type):
        utext = stext
    elif isinstance(stext, six.text_type):
        utext = stext
    else:
        try:
            utext = six.text_type(stext, encoding)
        except UnicodeDecodeError as err:
            if default_value is None:
                raise
            utext = default_value % {'error': err, 'value': ""}
    return utext

