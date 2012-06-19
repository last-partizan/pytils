# -*- coding: utf-8 -*-
# -*- test-case-name: pytils.test.test_numeral -*-
"""
Plural forms and in-word representation for numerals.
"""
from decimal import Decimal
from pytils import utils
from pytils.utils import takes, optional, list_of, tuple_of, \
                         nothing, one_of, check_positive, check_length

FRACTIONS = (
    (u"десятая", u"десятых", u"десятых"),
    (u"сотая", u"сотых", u"сотых"),
    (u"тысячная", u"тысячных", u"тысячных"),
    (u"десятитысячная", u"десятитысячных", u"десятитысячных"),
    (u"стотысячная", u"стотысячных", u"стотысячных"),
    (u"миллионная", u"милллионных", u"милллионных"),
    (u"десятимиллионная", u"десятимилллионных", u"десятимиллионных"),
    (u"стомиллионная", u"стомилллионных", u"стомиллионных"),
    (u"миллиардная", u"миллиардных", u"миллиардных"),
    )  #: Forms (1, 2, 5) for fractions

ONES = {
    0: (u"",       u"",       u""),
    1: (u"один",   u"одна",   u"одно"),
    2: (u"два",    u"две",    u"два"),
    3: (u"три",    u"три",    u"три"),
    4: (u"четыре", u"четыре", u"четыре"),
    5: (u"пять",   u"пять",   u"пять"),
    6: (u"шесть",  u"шесть",  u"шесть"),
    7: (u"семь",   u"семь",   u"семь"),
    8: (u"восемь", u"восемь", u"восемь"),
    9: (u"девять", u"девять", u"девять"),
    }  #: Forms (MALE, FEMALE, NEUTER) for ones

TENS = {
    0: u"",
    # 1 - особый случай
    10: u"десять",
    11: u"одиннадцать",
    12: u"двенадцать",
    13: u"тринадцать",
    14: u"четырнадцать",
    15: u"пятнадцать",
    16: u"шестнадцать",
    17: u"семнадцать",
    18: u"восемнадцать",
    19: u"девятнадцать",
    2: u"двадцать",
    3: u"тридцать",
    4: u"сорок",
    5: u"пятьдесят",
    6: u"шестьдесят",
    7: u"семьдесят",
    8: u"восемьдесят",
    9: u"девяносто",
    }  #: Tens

HUNDREDS = {
    0: u"",
    1: u"сто",
    2: u"двести",
    3: u"триста",
    4: u"четыреста",
    5: u"пятьсот",
    6: u"шестьсот",
    7: u"семьсот",
    8: u"восемьсот",
    9: u"девятьсот",
    }  #: Hundreds

MALE = 1    #: sex - male
FEMALE = 2  #: sex - female
NEUTER = 3  #: sex - neuter


@takes((int, long, float, Decimal),
       optional(int),
       signs=optional(int))
def _get_float_remainder(fvalue, signs=9):
    """
    Get remainder of float, i.e. 2.05 -> '05'

    @param fvalue: input value
    @type fvalue: C{int}, C{long}, C{float} or C{Decimal}

    @param signs: maximum number of signs
    @type signs: C{int} or C{long}

    @return: remainder
    @rtype: C{str}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (fvalue neither C{int}, no C{float})
    @raise ValueError: fvalue is negative
    @raise ValueError: signs overflow
    """
    check_positive(fvalue)
    if isinstance(fvalue, (int, long)):
        return "0"
    if isinstance(fvalue, Decimal) and fvalue.as_tuple()[2] == 0:
        # Decimal.as_tuple() -> (sign, digit_tuple, exponent)
        # если экспонента "0" -- значит дробной части нет
        return "0"

    signs = min(signs, len(FRACTIONS))

    # нужно remainder в строке, потому что дробные X.0Y
    # будут "ломаться" до X.Y
    remainder = str(fvalue).split('.')[1]
    iremainder = int(remainder)
    orig_remainder = remainder
    factor = len(str(remainder)) - signs

    if factor > 0:
        # после запятой цифр больше чем signs, округляем
        iremainder = int(round(iremainder / (10.0**factor)))
    format = "%%0%dd" % min(len(remainder), signs)

    remainder = format % iremainder

    if len(remainder) > signs:
        # при округлении цифр вида 0.998 ругаться
        raise ValueError("Signs overflow: I can't round only fractional part \
                          of %s to fit %s in %d signs" % \
                         (str(fvalue), orig_remainder, signs))

    return remainder


@takes((int,long), (unicode, list_of(unicode), tuple_of(unicode)))
def choose_plural(amount, variants):
    """
    Choose proper case depending on amount

    @param amount: amount of objects
    @type amount: C{int} or C{long}

    @param variants: variants (forms) of object in such form:
        (1 object, 2 objects, 5 objects).
    @type variants: 3-element C{sequence} of C{unicode}
        or C{unicode} (three variants with delimeter ',')

    @return: proper variant
    @rtype: C{unicode}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (amount isn't C{int}, variants isn't C{sequence})
    @raise ValueError: variants' length lesser than 3
    """
    
    if isinstance(variants, unicode):
        variants = utils.split_values(variants)
    check_length(variants, 3)
    amount = abs(amount)
    
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
         (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    else:
        variant = 2
    
    return variants[variant]

@takes((int,long),
       (unicode, list_of(unicode), tuple_of(unicode)),
        optional((nothing, unicode)),
        absence=optional((nothing, unicode)))
def get_plural(amount, variants, absence=None):
    """
    Get proper case with value

    @param amount: amount of objects
    @type amount: C{int} or C{long}

    @param variants: variants (forms) of object in such form:
        (1 object, 2 objects, 5 objects).
    @type variants: 3-element C{sequence} of C{unicode}
        or C{unicode} (three variants with delimeter ',')

    @param absence: if amount is zero will return it
    @type absence: C{unicode}

    @return: amount with proper variant
    @rtype: C{unicode}
    """
    if amount or absence is None:
        return u"%d %s" % (amount, choose_plural(amount, variants))
    else:
        return absence


@takes((int,long), (unicode, list_of(unicode), tuple_of(unicode)))
def _get_plural_legacy(amount, extra_variants):
    """
    Get proper case with value (legacy variant, without absence)

    @param amount: amount of objects
    @type amount: C{int} or C{long}

    @param variants: variants (forms) of object in such form:
        (1 object, 2 objects, 5 objects, 0-object variant).
        0-object variant is similar to C{absence} in C{get_plural}
    @type variants: 3-element C{sequence} of C{unicode}
        or C{unicode} (three variants with delimeter ',')

    @return: amount with proper variant
    @rtype: C{unicode}
    """
    absence = None
    if isinstance(extra_variants, unicode):
        extra_variants = utils.split_values(extra_variants)
    if len(extra_variants) == 4:
        variants = extra_variants[:3]
        absence = extra_variants[3]
    else:
        variants = extra_variants
    return get_plural(amount, variants, absence)

@takes((int, long, float, Decimal), optional(bool), zero_for_kopeck=optional(bool))
def rubles(amount, zero_for_kopeck=False):
    """
    Get string for money

    @param amount: amount of money
    @type amount: C{int}, C{long}, C{float} or C{Decimal}

    @param zero_for_kopeck: If false, then zero kopecks ignored
    @type zero_for_kopeck: C{bool}

    @return: in-words representation of money's amount
    @rtype: C{unicode}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (amount neither C{int}, no C{float})
    @raise ValueError: amount is negative
    """
    check_positive(amount)

    pts = []
    amount = round(amount, 2)
    pts.append(sum_string(int(amount), 1, (u"рубль", u"рубля", u"рублей")))
    remainder = _get_float_remainder(amount, 2)
    iremainder = int(remainder)

    if iremainder != 0 or zero_for_kopeck:
        # если 3.1, то это 10 копеек, а не одна
        if iremainder < 10 and len(remainder) == 1:
            iremainder *= 10
        pts.append(sum_string(iremainder, 2,
                              (u"копейка", u"копейки", u"копеек")))

    return u" ".join(pts)


@takes((int,long), optional(one_of(1,2,3)), gender=optional(one_of(1,2,3)))
def in_words_int(amount, gender=MALE):
    """
    Integer in words

    @param amount: numeral
    @type amount: C{int} or C{long}

    @param gender: gender (MALE, FEMALE or NEUTER)
    @type gender: C{int}

    @return: in-words reprsentation of numeral
    @rtype: C{unicode}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (when amount is not C{int})
    @raise ValueError: amount is negative
    """
    check_positive(amount)

    return sum_string(amount, gender)

@takes((float, Decimal), optional(one_of(1,2,3)), _gender=optional(one_of(1,2,3)))
def in_words_float(amount, _gender=FEMALE):
    """
    Float in words

    @param amount: float numeral
    @type amount: C{float} or C{Decimal}

    @return: in-words reprsentation of float numeral
    @rtype: C{unicode}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
        (when amount is not C{float})
    @raise ValueError: when ammount is negative
    """
    utils.check_positive(amount)

    pts = []
    # преобразуем целую часть
    pts.append(sum_string(int(amount), 2,
                          (u"целая", u"целых", u"целых")))
    # теперь то, что после запятой
    remainder = _get_float_remainder(amount)
    signs = len(str(remainder)) - 1
    pts.append(sum_string(int(remainder), 2, FRACTIONS[signs]))

    return u" ".join(pts)

@takes((int,long,float,Decimal),
       optional(one_of(None,1,2,3)),
       gender=optional(one_of(None,1,2,3)))
def in_words(amount, gender=None):
    """
    Numeral in words

    @param amount: numeral
    @type amount: C{int}, C{long}, C{float} or C{Decimal}

    @param gender: gender (MALE, FEMALE or NEUTER)
    @type gender: C{int}

    @return: in-words reprsentation of numeral
    @rtype: C{unicode}

    raise L{pytils.err.InputParameterError}: input parameters' check failed
        (when amount not C{int} or C{float}, gender is not C{int} (and not None),
         gender isn't in (MALE, FEMALE, NEUTER))
    raise ValueError: when amount is negative
    """
    check_positive(amount)
    if isinstance(amount, Decimal) and amount.as_tuple()[2] == 0:
        # если целое,
        # т.е. Decimal.as_tuple -> (sign, digits tuple, exponent), exponent=0
        # то как целое
        amount = int(amount)
    if gender is None:
        args = (amount,)
    else:
        args = (amount, gender)
    # если целое
    if isinstance(amount, (int, long)):
        return in_words_int(*args)
    # если дробное
    elif isinstance(amount, (float, Decimal)):
        return in_words_float(*args)
    # ни float, ни int, ни Decimal
    else:
        # до сюда не должно дойти
        raise RuntimeError()

@takes((int, long),
       one_of(1, 2, 3),
       optional((unicode, nothing, list_of(unicode), tuple_of(unicode))),
       items=optional((unicode, nothing, list_of(unicode), tuple_of(unicode))))
def sum_string(amount, gender, items=None):
    """
    Get sum in words

    @param amount: amount of objects
    @type amount: C{int} or C{long}

    @param gender: gender of object (MALE, FEMALE or NEUTER)
    @type gender: C{int}

    @param items: variants of object in three forms:
        for one object, for two objects and for five objects
    @type items: 3-element C{sequence} of C{unicode} or
        just C{unicode} (three variants with delimeter ',')

    @return: in-words representation objects' amount
    @rtype: C{unicode}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
    @raise ValueError: items isn't 3-element C{sequence} or C{unicode}
    @raise ValueError: amount bigger than 10**36-1
    @raise ValueError: amount is negative
    """
    if isinstance(items, unicode):
        items = utils.split_values(items)
    if items is None:
        items = (u"", u"", u"")

    try:
        one_item, two_items, five_items = items
    except ValueError:
        raise ValueError("Items must be 3-element sequence")

    check_positive(amount)

    if amount == 0:
        return u"ноль %s" % five_items

    into = u''
    tmp_val = amount

    # единицы
    into, tmp_val = _sum_string_fn(into, tmp_val, gender, items)
    names = (
        (FEMALE, (u"тысяча", u"тысячи", u"тысяч")), # тысячи
        (MALE,   (u"миллион", u"миллиона", u"миллионов")), # миллионы
        (MALE,   (u"миллиард", u"миллиарда", u"миллиардов")), # миллиарды
        (MALE,   (u"триллион", u"триллиона", u"триллионов")), # триллионы
        (MALE,   (u"квадриллион", u"квадриллиона", u"квадриллионов")), # квадриллионы
        (MALE,   (u"квинтиллион", u"квинтиллиона", u"квинтиллионов")), # квинтиллион
        (MALE,   (u"секстилион", u"секстилиона", u"секстилионов")), # секстилион
        (MALE,   (u"септиллион", u"септиллиона", u"септиллионов")), # септиллион
        (MALE,   (u"октиллион", u"октиллиона", u"октиллионов")), # октиллион
        (MALE,   (u"нониллион", u"нониллиона", u"нониллионов")), # нониллион
        (MALE,   (u"дециллион", u"дециллиона", u"дециллионов")), # дециллион
    )
    for name in names:
        into, tmp_val = _sum_string_fn(into, tmp_val, *name)
        if tmp_val == 0:
            return into
    raise ValueError("Cannot operand with numbers bigger than 10**36-1")

@takes(unicode,
       (int,long),
       one_of(1,2,3),
       optional((unicode, nothing, list_of(unicode), tuple_of(unicode))),
       items=optional((unicode, nothing, list_of(unicode), tuple_of(unicode))))
def _sum_string_fn(into, tmp_val, gender, items=None):
    """
    Make in-words representation of single order

    @param into: in-words representation of lower orders
    @type into: C{unicode}

    @param tmp_val: temporary value without lower orders
    @type tmp_val: C{int} or C{long}

    @param gender: gender (MALE, FEMALE or NEUTER)
    @type gender: C{int}

    @param items: variants of objects
    @type items: 3-element C{sequence} of C{unicode}

    @return: new into and tmp_val
    @rtype: C{tuple}

    @raise L{pytils.err.InputParameterError}: input parameters' check failed
    @raise ValueError: tmp_val is negative
    """
    if items is None:
        items = (u"", u"", u"")
    one_item, two_items, five_items = items
    
    check_positive(tmp_val)

    if tmp_val == 0:
        return into, tmp_val

    words = []

    rest = tmp_val % 1000
    tmp_val = tmp_val / 1000
    if rest == 0:
        # последние три знака нулевые
        if into == u"":
            into = u"%s " % five_items
        return into, tmp_val

    # начинаем подсчет с rest
    end_word = five_items

    # сотни
    words.append(HUNDREDS[rest / 100])

    # десятки
    rest = rest % 100
    rest1 = rest / 10
    # особый случай -- tens=1
    tens = rest1 == 1 and TENS[rest] or TENS[rest1]
    words.append(tens)

    # единицы
    if rest1 < 1 or rest1 > 1:
        amount = rest % 10
        end_word = choose_plural(amount, items)
        words.append(ONES[amount][gender-1])
    words.append(end_word)

    # добавляем то, что уже было
    words.append(into)

    # убираем пустые подстроки
    words = filter(lambda x: len(x) > 0, words)

    # склеиваем и отдаем
    return u" ".join(words).strip(), tmp_val
