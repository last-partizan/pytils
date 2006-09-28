# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
pytils.translit templatetags for Django web-framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

from django import template, conf
from pytils import translit, utils

register = template.Library()
encoding = conf.settings.DEFAULT_CHARSET

# -- filters --

def translify(stext):
    """Translify russian text"""
    try:
        res = translit.translify(
            utils.provide_unicode(stext, encoding))
    except Exception, err:
        # because filter must die silently
        res = "unknown"
    return res

def detranslify(stext):
    """Detranslify russian text"""
    try:
        res = utils.provide_str(
            translit.detranslify(stext),
            encoding)
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res

def slugify(stext):
    """Make slug from text"""
    try:
        res = translit.slugify(
            utils.provide_unicode(stext, encoding))
    except Exception:
        # because filter must die silently
        res = "unknown"
    return res

# -- register filters
register.filter('translify', translify)
register.filter('detranslify', detranslify)
register.filter('slugify', slugify)
