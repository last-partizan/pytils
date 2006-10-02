# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_translit -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Simple transliteration
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import re

TRANSTABLE = (
        (u"№", u"#"),
        ## верхний регистр
        # трехбуквенные замены
        (u"Щ", u"Sch"),
        # при замене русский->английский будет первая замена,
        # т.е. Sch
        # а вот если английский->русский, то вариант SCH и Sch --
        # оба пройдут
        (u"Щ", u"SCH"), 
        # двухбуквенные замены
        (u"Ё", u"Yo"),
        (u"Ё", u"YO"),
        (u"Ж", u"Zh"),
        (u"Ж", u"ZH"),
        (u"Ц", u"Ts"),
        (u"Ц", u"TS"),
        (u"Ч", u"Ch"),
        (u"Ч", u"CH"),
        (u"Ш", u"Sh"),
        (u"Ш", u"SH"),
        (u"Ы", u"Yi"),
        (u"Ы", u"YI"),
        (u"Ю", u"Yu"),
        (u"Ю", u"YU"),
        (u"Я", u"Ya"),
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
        )

def translify(in_string):
    """
    Translify russian text

    @param in_string: input string
    @type in_string: C{unicode}
    
    @return: transliterated string
    @rtype: C{str}

    @raise TypeError: when in_string is not C{unicode}
    @raise ValueError: when string doesn't transliterate completely
    """
    if not isinstance(in_string, unicode):
        raise TypeError("Expects unicode, but got %s" % type(in_string))

    translit = in_string
    for symb_in, symb_out in TRANSTABLE:
        translit = translit.replace(symb_in, symb_out)

    try:
        translit = str(translit)
    except UnicodeEncodeError:
        raise ValueError("Unicode string doesn't transliterate completely, " + \
                         "is it russian?")

    return translit

def detranslify(in_string):
    """
    Detranslify

    @param in_string: input string
    @type in_string: C{basestring}
    
    @return: detransliterated string
    @rtype: C{str}

    @raise TypeError: when in_string neither C{str}, no C{unicode}
    @raise ValueError: if in_string is C{str}, but it isn't ascii
    """
    if not isinstance(in_string, basestring):
        raise TypeError("Expects basestring, but got %s" % type(in_string))

    # в unicode
    try:
        russian = unicode(in_string)
    except UnicodeDecodeError:
        raise ValueError("We expects when in_string is str type," + \
                         "it is an ascii, but now it isn't. Use unicode " + \
                         "in this case.")

    for symb_out, symb_in in TRANSTABLE:
        russian = russian.replace(symb_in, symb_out)

    return russian

def slugify(in_string):
    """
    Prepare string for slug (i.e. URL or file/dir name)

    @param in_string: input string
    @type in_string: C{basestring}

    @return: slug-string
    @rtype: C{str}

    @raise TypeError: when in_string isn't C{unicode} or C{str}
    @raise ValueError: if in_string is C{str}, but it isn't ascii
    """
    if not isinstance(in_string, basestring):
        raise TypeError("Expects basestring, but got %s" % type(in_string))
    try:
        u_in_string = unicode(in_string)
    except UnicodeDecodeError:
        raise ValueError("We expects when in_string is str type," + \
                         "it is an ascii, but now it isn't. Use unicode " + \
                         "in this case.")
    
    st = translify(u_in_string)

    # convert & to "and"
    st = re.sub('\&amp\;|\&', ' and ', st)
    # remove non-alpha
    st = re.sub('[^\w\s-]', '', st).strip().lower()
    # replace spaces by hyphen
    return re.sub('[-\s]+', '-', st)
        
def dirify(in_string):
    """
    Alias for L{slugify}
    """
    slugify(in_string)

