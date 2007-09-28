# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_utils -*-
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
Misc utils for internal use
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import sys

from third.aspn426123 import takes, returns, optional, one_of, list_of, tuple_of, \
                             nothing, anything

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

def split_values(ustring, sep=u','):
    """
    Splits unicode string with separator C{sep},
    but skips escaped separator.
    
    @param ustring: string to split
    @type ustring: C{unicode}
    
    @param sep: separator (default to u',')
    @type sep: C{unicode}
    
    @return: tuple of splitted elements
    """
    assert isinstance(ustring, unicode), "uvalue must be unicode, not %s" % type(ustring)
    # в юникоде есть специальный символ, который в нормальном тексте не должен встречаться
    # это маркер 0xffff
    # им и будем помечать места, где есть экранированная запятая
    ustring_marked = ustring.replace(u'\,', u'\uffff')
    items = tuple([i.strip().replace(u'\uffff', u',') for i in ustring_marked.split(sep)])
    return items
