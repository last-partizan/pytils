# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.templatetags.test_translit -*-
# pytils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
#
# http://www.pyobject.ru/projects/pytils/
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
pytils.translit templatetags for Django web-framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from django import template, conf
from pytils import translit, utils

register = template.Library()  #: Django template tag/filter registrator
encoding = conf.settings.DEFAULT_CHARSET  #: Current charset (sets in Django project's settings)
debug = conf.settings.DEBUG  #: Debug mode (sets in Django project's settings)
show_value = getattr(conf.settings, 'PYTILS_SHOW_VALUES_ON_ERROR', False)  #: Show values on errors (sets in Django project's settings)

# Если отладка, то показываем 'unknown+сообщение об ошибке'.
# Если отладка выключена, то можно чтобы при ошибках показывалось
# значение, переданное фильтру (PYTILS_SHOW_VALUES_ON_ERROR=True)
# либо пустая строка.

if debug:
    default_value = "unknown: %(error)s"
    default_uvalue = u"unknown: %(error)s"
elif show_value:
    default_value = "%(value)s"
    default_uvalue = u"%(value)s"
else:
    default_value = ""
    default_uvalue = u""


# -- filters --

def translify(stext):
    """Translify russian text"""
    try:
        res = translit.translify(
            utils.provide_unicode(
                stext,
                encoding,
                default=default_value
                ))
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': stext}
    return res

def detranslify(stext):
    """Detranslify russian text"""
    try:
        res = utils.provide_str(
            translit.detranslify(stext),
            encoding,
            default=default_uvalue)
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': stext}
    return res

def slugify(stext):
    """Make slug from (russian) text"""
    try:
        res = translit.slugify(
            utils.provide_unicode(
                stext,
                encoding,
                default=default_value
                ))
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': stext}
    return res

# -- register filters
register.filter('translify', translify)
register.filter('detranslify', detranslify)
register.filter('slugify', slugify)
