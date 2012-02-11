# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.templatetags.test_translit -*-
"""
pytils.translit templatetags for Django web-framework
"""

from django import template, conf
from pytils import translit
from pytils.templatetags import pseudo_str, pseudo_unicode, init_defaults

register = template.Library()  #: Django template tag/filter registrator
encoding = conf.settings.DEFAULT_CHARSET  #: Current charset (sets in Django project's settings)
debug = conf.settings.DEBUG  #: Debug mode (sets in Django project's settings)
show_value = getattr(conf.settings, 'PYTILS_SHOW_VALUES_ON_ERROR', False)  #: Show values on errors (sets in Django project's settings)

default_value, default_uvalue = init_defaults(debug, show_value)

# -- filters --

def translify(stext):
    """Translify russian text"""
    try:
        utext = pseudo_unicode(
                        stext,
                        encoding,
                        default_value)
        res = translit.translify(utext)
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': stext}
    return res

def detranslify(stext):
    """Detranslify russian text"""
    try:
        ures = translit.detranslify(stext)
        res = pseudo_str(
                ures,
                encoding,
                default_uvalue)
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': stext}
    return res

def slugify(stext):
    """Make slug from (russian) text"""
    try:
        utext = pseudo_unicode(
                stext,
                encoding,
                default_value)
        res = translit.slugify(utext)
    except Exception, err:
        # because filter must die silently
        res = default_value % {'error': err, 'value': stext}
    return res

# -- register filters
register.filter('translify', translify)
register.filter('detranslify', detranslify)
register.filter('slugify', slugify)
