# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_translit -*-
# pytils - russian-specific string utils
# Copyright (C) 2006-2009  Yury Yurevich
#
# http://pyobject.ru/projects/pytils/
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
from __future__ import print_function, absolute_import, division, unicode_literals
"""
Simple transliteration
"""

import re
from pytils.utils import takes, returns

TRANSTABLE = (
        ("'", "'"),
        ('"', '"'),
        ("‘", "'"),
        ("’", "'"),
        ("«", '"'),
        ("»", '"'),
        ("“", '"'),
        ("”", '"'),
        ("–", "-"),  # en dash
        ("—", "-"),  # em dash
        ("‒", "-"),  # figure dash
        ("−", "-"),  # minus
        ("…", "..."),
        ("№", "#"),
        ## upper
        # three-symbols replacements
        ("Щ", "Sch"),
        # on russian->english translation only first replacement will be done
        # i.e. Sch
        # but on english->russian translation both variants (Sch and SCH) will play
        ("Щ", "SCH"),
        # two-symbol replacements
        ("Ё", "Yo"),
        ("Ё", "YO"),
        ("Ж", "Zh"),
        ("Ж", "ZH"),
        ("Ц", "Ts"),
        ("Ц", "TS"),
        ("Ч", "Ch"),
        ("Ч", "CH"),
        ("Ш", "Sh"),
        ("Ш", "SH"),
        ("Ы", "Yi"),
        ("Ы", "YI"),
        ("Ю", "Y"),
        ("Ю", "YU"),
        ("Я", "Ya"),
        ("Я", "YA"),
        # one-symbol replacements
        ("А", "A"),
        ("Б", "B"),
        ("В", "V"),
        ("Г", "G"),
        ("Д", "D"),
        ("Е", "E"),
        ("З", "Z"),
        ("И", "I"),
        ("Й", "J"),
        ("К", "K"),
        ("Л", "L"),
        ("М", "M"),
        ("Н", "N"),
        ("О", "O"),
        ("П", "P"),
        ("Р", "R"),
        ("С", "S"),
        ("Т", "T"),
        ("У", "U"),
        ("Ф", "F"),
        ("Х", "H"),
        ("Э", "E"),
        ("Ъ", "`"),
        ("Ь", "'"),
        ## lower
        # three-symbols replacements
        ("щ", "sch"),
        # two-symbols replacements
        ("ё", "yo"),
        ("ж", "zh"),
        ("ц", "ts"),
        ("ч", "ch"),
        ("ш", "sh"),
        ("ы", "yi"),
        ("ю", "y"),
        ("я", "ya"),
        # one-symbol replacements
        ("а", "a"),
        ("б", "b"),
        ("в", "v"),
        ("г", "g"),
        ("д", "d"),
        ("е", "e"),
        ("з", "z"),
        ("и", "i"),
        ("й", "j"),
        ("к", "k"),
        ("л", "l"),
        ("м", "m"),
        ("н", "n"),
        ("о", "o"),
        ("п", "p"),
        ("р", "r"),
        ("с", "s"),
        ("т", "t"),
        ("у", ""),
        ("ф", "f"),
        ("х", "h"),
        ("э", "e"),
        ("ъ", "`"),
        ("ь", "'"),
        # Make english alphabet full: append english-english pairs
        # for symbols which is not used in russian-english
        # translations. Used in slugify.
        ("c", "c"),
        ("q", "q"),
        ("y", "y"),
        ("x", "x"),
        ("w", "w"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("0", "0"),
        )  #: Translation table

RU_ALPHABET = [x[0] for x in TRANSTABLE] #: Russian alphabet that we can translate
EN_ALPHABET = [x[1] for x in TRANSTABLE] #: English alphabet that we can detransliterate
ALPHABET = RU_ALPHABET + EN_ALPHABET #: Alphabet that we can (de)transliterate

@takes(unicode)
@returns(str)
def translify(in_string):
    """
    Translify russian text

    @param in_string: input string
    @type in_string: C{unicode}

    @return: transliterated string
    @rtype: C{str}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (in_string is not C{unicode})
    @raise ValueError: when string doesn't transliterate completely
    """
    translit = in_string
    for symb_in, symb_out in TRANSTABLE:
        translit = translit.replace(symb_in, symb_out)

    try:
        translit = str(translit)
    except UnicodeEncodeError:
        raise ValueError("Unicode string doesn't transliterate completely, " + \
                         "is it russian?")

    return translit

@takes(basestring)
@returns(unicode)
def detranslify(in_string):
    """
    Detranslify

    @param in_string: input string
    @type in_string: C{basestring}

    @return: detransliterated string
    @rtype: C{unicode}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (when in_string not C{basestring})
    @raise ValueError: if in_string is C{str}, but it isn't ascii
    """
    # в unicode
    try:
        russian = unicode(in_string)
    except UnicodeDecodeError:
        raise ValueError("We expects if in_string is 8-bit string," + \
                         "then it consists only ASCII chars, but now it doesn't. " + \
                         "Use unicode in this case.")

    for symb_out, symb_in in TRANSTABLE:
        russian = russian.replace(symb_in, symb_out)

    return russian

@takes(basestring)
@returns(str)
def slugify(in_string):
    """
    Prepare string for slug (i.e. URL or file/dir name)

    @param in_string: input string
    @type in_string: C{basestring}

    @return: slug-string
    @rtype: C{str}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (when in_string isn't C{unicode} or C{str})
    @raise ValueError: if in_string is C{str}, but it isn't ascii
    """
    try:
        u_in_string = unicode(in_string).lower()
    except UnicodeDecodeError:
        raise ValueError("We expects when in_string is str type," + \
                         "it is an ascii, but now it isn't. Use unicode " + \
                         "in this case.")
    # convert & to "and"
    u_in_string = re.sub('\&amp\;|\&', ' and ', u_in_string)
    # replace spaces by hyphen
    u_in_string = re.sub('[-\s]+', '-', u_in_string)
    # remove symbols that not in alphabet
    u_in_string = ''.join([symb for symb in u_in_string if symb in ALPHABET])
    # translify it
    out_string = translify(u_in_string)
    # remove non-alpha
    return re.sub('[^\w\s-]', '', out_string).strip().lower()


def dirify(in_string):
    """
    Alias for L{slugify}
    """
    slugify(in_string)
