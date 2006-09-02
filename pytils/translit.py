# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_translit -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Simple transliteration
"""

__id__ = "$Id$"
__url__ = "$URL$"

import re

TRANSTABLE = (
        (u"№", u"#"),
        ## нижний регистр
        # трехбуквенные замены
        (u"щ", u"sch"),
        # двухбуквенные замены
        (u"ё", u"yo"),
        (u"ж", u"zh"),
        (u"ц", u"ts"),
        (u"ч", u"ch"),
        (u"ш", u"sh"),
        (u"ы", u"yi"),
        (u"ю", u"yu"),
        (u"я", u"ya"),
        # однобуквенные замены
        (u"а", u"a"),
        (u"б", u"b"),
        (u"в", u"v"),
        (u"г", u"g"),
        (u"д", u"d"),
        (u"е", u"e"),
        (u"з", u"z"),
        (u"и", u"i"),
        (u"й", u"j"),
        (u"к", u"k"),
        (u"л", u"l"),
        (u"м", u"m"),
        (u"н", u"n"),
        (u"о", u"o"),
        (u"п", u"p"),
        (u"р", u"r"),
        (u"с", u"s"),
        (u"т", u"t"),
        (u"у", u"u"),
        (u"ф", u"f"),
        (u"х", u"h"),
        (u"э", u"e"),
        (u"ъ", u"`"),
        (u"ь", u"'"),
        ## верхний регистр
        # трехбуквенные замены
        (u"Щ", u"SCH"),
        # двухбуквенные замены
        (u"Ё", u"YO"),
        (u"Ж", u"ZH"),
        (u"Ц", u"TS"),
        (u"Ч", u"CH"),
        (u"Ш", u"SH"),
        (u"Ы", u"YI"),
        (u"Ю", u"YU"),
        (u"Я", u"YA"),
        # однобуквенные замены
        (u"А", u"A"),
        (u"Б", u"B"),
        (u"В", u"V"),
        (u"Г", u"G"),
        (u"Д", u"D"),
        (u"Е", u"E"),
        (u"З", u"Z"),
        (u"И", u"I"),
        (u"Й", u"J"),
        (u"К", u"K"),
        (u"Л", u"L"),
        (u"М", u"M"),
        (u"Н", u"N"),
        (u"О", u"O"),
        (u"П", u"P"),
        (u"Р", u"R"),
        (u"С", u"S"),
        (u"Т", u"T"),
        (u"У", u"U"),
        (u"Ф", u"F"),
        (u"Х", u"H"),
        (u"Э", u"E"),
        (u"Ъ", u"`"),
        (u"Ь", u"'"),
        )

def translify(in_string):
    """
    Translify russian text

    @param in_string: input string
    @type in_string: unicode
    
    @return: transliterated string
    @rtype: str
    """
    assert isinstance(in_string, unicode)

    s = in_string
    for symb_in, symb_out in TRANSTABLE:
        s = s.replace(symb_in, symb_out)

    # в str
    # в этом моменте может произойти UnicodeError
    # если не всё перекодировалось
    s = str(s)

    return s

def detranslify(in_string):
    """
    Detranslify

    @param in_string: input string
    @type in_string: basestring
    
    @return: detransliterated string
    @rtype: str
    """

    assert isinstance(in_string, basestring)

    # в unicode
    # в этом моменте може произойти UnicodeError
    # если передан не-ascii 
    s = unicode(in_string)

    for symb_out, symb_in in TRANSTABLE:
        s = s.replace(symb_in, symb_out)

    return s

def slugify(in_string):
    """
    Prepare string for slug (i.e. URL or file/dir name)

    @param in_string: input string
    @type in_string: unicode

    @return: slug-string
    @rtype: str
    """
    assert isinstance(in_string, unicode)
    
    st = translify(in_string)

    # convert & to "and"
    st = re.sub('\&amp\;|\&', ' and ', st)
    # remove non-alpha
    st = re.sub('[^\w\s-]', '', st).strip().lower()
    # replace spaces by hyphen
    return re.sub('[-\s]+', '-', st)
        
def dirify(in_string):
    """
    Alias for slugify
    """
    slugify(in_string)

