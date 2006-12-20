# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_utils -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Misc utils for internal use
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import sys


def provide_unicode(stext, encoding, default=u"неизвестно"):
    """
    Provide Unicode from text

    @param stext: text
    @type stext: C{str}

    @param encoding: encoding if input text
    @type encoding: C{str}

    @return: C{unicode}
    """
    try:
        utext = str(stext).decode(encoding)
    except UnicodeDecodeError, err:
        utext = default % {'error': err, 'value': u""}
    return utext


def provide_str(utext, encoding, default="unknown"):
    """
    Provide text from Unicode

    @param utext: unicode text
    @type utext: C{unicode}

    @param encoding: encoding of output text
    @type encoding: C{str}

    @return: C{str}
    """
    try:
        stext = unicode(utext).encode(encoding)
    except UnicodeEncodeError, err:
        stext = default % {'error': err, 'value': ""}
    return stext


def get_value_by_name(variable_name, depth=1):
    """
    Return value of variable by it's name

    @param variable_name: name of variable
    @type variable_name: C{str}

    @param depth: stack depth
    @type depth: C{int}

    @raise RuntimeError: when unable to fetch variable
    """
    try:
        variable_value = sys._getframe(depth).f_locals[variable_name]
    except KeyError:
        raise RuntimeError("Unable to fetch variable %s (depth %d)" % \
                           (variable_name, depth))
    return variable_value


def check_type(variable_name, typ):
    """
    Checks type of variable

    @param variable_name: name of variable
    @type variable_name: C{str}

    @param typ: type checking for
    @type typ: C{type} or C{tuple} of types

    @return: None when check successful

    @raise TypeError: check failed
    """
    variable_value = get_value_by_name(variable_name, 2)
    if not isinstance(variable_value, typ):
        raise TypeError("%s must be %s, not %s" % \
                        (variable_name, str(typ), type(variable_value)))


def check_length(variable_name, length):
    """
    Checks length of variable's value

    @param variable_name: name of variable
    @type variable_name: C{str}

    @param length: length checking for
    @type length: C{int}

    @return: None when check successful

    @raise ValueError: check failed
    """
    variable_value = get_value_by_name(variable_name, 2)
    _length = len(variable_value)
    if _length != length:
        raise ValueError("%s's length must be %d, but it %d" % \
                         (variable_name, length, _length))


def check_positive(variable_name, strict=False):
    """
    Checks if variable is positive

    @param variable_name: name of variable
    @type variable_name: C{str}

    @return: None when check successful

    @raise ValueError: check failed
    """
    variable_value = get_value_by_name(variable_name, 2)
    if not strict and variable_value < 0:
        raise ValueError("%s must be positive or zero, not %s" % \
                         (variable_name, str(variable_value)))
    if strict and variable_value <= 0:
        raise ValueError("%s must be positive, not %s" % \
                         (variable_name, str(variable_value)))
