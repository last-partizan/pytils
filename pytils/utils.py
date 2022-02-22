# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_utils -*-
"""
Misc utils for internal use
"""


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


def check_positive(value, strict=False):
    """
    Checks if variable is positive

    @param value: value to check
    @type value: C{integer types}, C{float} or C{Decimal}

    @return: None when check successful

    @raise ValueError: check failed
    """
    if not strict and value < 0:
        raise ValueError("Value must be positive or zero, not %s" % str(value))
    if strict and value <= 0:
        raise ValueError("Value must be positive, not %s" % str(value))


def split_values(ustring, sep=','):
    """
    Splits unicode string with separator C{sep},
    but skips escaped separator.
    
    @param ustring: string to split
    @type ustring: C{str}
    
    @param sep: separator (default to ',')
    @type sep: C{str}
    
    @return: tuple of splitted elements
    """
    assert isinstance(ustring, str), "uvalue must be str, not %s" % type(ustring)
    # unicode have special mark symbol 0xffff which cannot be used in a regular text,
    # so we use it to mark a place where escaped column was
    ustring_marked = ustring.replace('\,', '\uffff')
    items = tuple([i.strip().replace('\uffff', ',') for i in ustring_marked.split(sep)])
    return items
