pytils - простой обработчик русского текста.
==========================================================

Кратко
------

pytils - простой обработчик русского текста, реализован на Python. 
Идея позаимствована у [Julik](http://live.julik.nl) и его 
[RuTils](http://rutils.rubyforge.org/).

Ссылки
------

 *  [pytils на github](http://github.com/j2a/pytils/)

Как установить
--------------

Смотрите INSTALL (или INSTALL.rus.txt)

Как использовать
----------------

Во-первых, **все** входящие строки - unicode. И выходящие - тоже (за малыми
исключениями, о них ниже). В случае, если Вы передадите str, получите
AssertionError.

pytils содержит следующие модули: 

 1.  `numeral` - для обработки числительных
 2.  `dt` - русские даты без локалей
 3.  `translit` - транслитерация

pytils легко интегрируется с популярными  Web-фреймворками (Django, Flask),
подробнее об этом смотрите в WEBFRAMEWORKS.rus.txt.

Примеры смотрите в каталоге examples.

Числительные
------------

pytils умеет выбирать правильный падеж в зависимости от числа

    >>> pytils.numeral.choose_plural(15, (u"гвоздь", u"гвоздя", u"гвоздей"))
    u'гвоздей'


В качестве второго параметра передается кортеж с вариантами (либо строка, 
где варианты перечисляются через запятую). Чтобы легко запомнить, 
в каком порядке указывать варианты, пользуйтесь мнемоническим 
правилом: один-два-пять - один гвоздь, два гвоздя, пять гвоздей.

Часто нужен не просто вариант, а число вместе с текстом

    >>> pytils.numeral.get_plural(15, u"гвоздь, гвоздя, гвоздей")
    u'15 гвоздей'

В get_plural можно еще передать вариант, когда число -- ноль. Т.е. чтобы
было не '0 гвоздей', а 'гвоздей нет':

    >>> pytils.numeral.get_plural(0, u"гвоздь, гвоздя, гвоздей")
    u'0 гвоздей'
    >>> pytils.numeral.get_plural(0, u"гвоздь, гвоздя, гвоздей", absence=u"гвоздей нет")
    u'гвоздей нет'


Также pytils реализует числа прописью

    >>> pytils.numeral.in_words(254)
    u'двести пятьдесят четыре'
    >>> pytils.numeral.in_words(2.01)
    u'две целых одна сотая'
    >>> pytils.numeral.rubles(2.01)
    u'два рубля одна копейка'
    >>> pytils.numeral.sum_string(32, pytils.numeral.MALE, (u"гвоздь", u"гвоздя", u"гвоздей"))
    u'тридцать два гвоздя'
    >>> pytils.numeral.sum_string(21, pytils.numeral.FEMALE, u"белка, белки, белок")
    u'двадцать одна белка'

Даты
----

В pytils можно получить русские даты без использования локалей.

    >>> pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True, date=datetime.date(2006, 9, 2))
    u'сегодня - 2 сентября 2006, суббота'

    >>> pytils.dt.ru_strftime(u"сделано %A, %d %B %Y", inflected=True, preposition=True)
    u'сделано во вторник, 10 июля 2007'

Есть возможность получить величину периода:

    >>> pytils.dt.distance_of_time_in_words(time.time()-10000)
    u'2 часа назад'
    >>> pytils.dt.distance_of_time_in_words(datetime.datetime.now()+datetime.timedelta(0,10000), accuracy=2)
    u'через 2 часа 46 минут'

Транслитерация
--------------

При помощи pytils можно сделать транслитерацию:

    >>> print(pytils.translit.translify(u"Проверка связи"))
    'Proverka svyazi'
    >>> pytils.translit.detranslify("Proverka svyazi")
    u'Проверка связи'

В translify вывод - str, а не unicode. В detranslify вход может быть как 
unicode, так и str.

И сделать строку для URL (удаляются лишние символы, пробелы заменяются на 
дефисы):

    >>> pytils.translit.slugify(u"тест и еще раз тест")
    'test-i-esche-raz-test'

