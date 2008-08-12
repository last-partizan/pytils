# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_utils -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2008  Yury Yurevich
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

import sys
import warnings

from pytils.third.aspn426123 import takes, returns, optional, list_of, tuple_of, \
                                    nothing, one_of


@takes((basestring, tuple, list), (int, long))
def check_length(value, length):
    """
    Checks length of value

    @param value: value to check
    @type value: C{str}

    @param length: length checking for
    @type length: C{int}

    @return: None when check successful

    @raise ValueError: check failed
    """
    _length = len(value)
    if _length != length:
        raise ValueError("length must be %d, not %d" % \
                         (length, _length))


@takes((int,long,float), optional(bool), strict=optional(bool))
def check_positive(value, strict=False):
    """
    Checks if variable is positive

    @param value: value to check
    @type value: C{int}, C{long} or C{float}

    @return: None when check successful

    @raise ValueError: check failed
    """
    if not strict and value < 0:
        raise ValueError("Value must be positive or zero, not %s" % str(value))
    if strict and value <= 0:
        raise ValueError("Value must be positive, not %s" % str(value))


@takes(unicode, optional(unicode), sep=optional(unicode))
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
