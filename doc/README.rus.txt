ID: $Id$

PyTils - библиотека для простой обработки русского текста.
==========================================================

Кратко
------

PyTils - простой обработчик русского текста на Python. Идея позаимствована у 
[Julik](http://live.julik.nl) и его [RuTils](http://rutils.rubyforge.org/).

Автор PyTils - [Pythy](mailto:the.pythy@gmail.com).

Ссылки
------

 *  [Pythy на code.google.com](http://code.google.com/p/pythy/)
 *  [Пост о PyTils в блоге](http://gorod-omsk.ru/blog/pythy/2006/09/02/pytils/)
 *  [Страница PyTils](http://gorod-omsk.ru/blog/pythy/projects/pytils/)

Как установить
--------------

Смотрите INSTALL (или INSTALL.rus.txt)

Как использовать
----------------

Во-первых, **все** входящие строки - unicode. И выходящие - тоже (за малыми
исключениями, о них ниже). В случае, если Вы передадите str, получите
AssertionError.

PyTils содержит следующие модули: 

 1.  `numeral` - для обработки числительных
 2.  `dt` - русские даты без локалей
 3.  `translit` - транслитерация

API модулей смотрите в директории [api](api/index.html).

PyTils легко интегрируется с популярными  Web-фреймворками (Django, TurboGears),
подробнее об этом смотрите в WEBFRAMEWORKS.rus.txt.

Примеры смотрите в каталоге examples.

Числительные
------------

PyTils умеет выбирать правильный падеж в зависимости от числа

    >>> pytils.numeral.choose_plural(15, (u"гвоздь", u"гвоздя", u"гвоздей"))
    u'гвоздей'

В качестве второго параметра передается кортеж с вариантами. Чтобы легко 
запомнить, в каком порядке указывать варианты, пользуйтесь мнемоническим 
правилом: один-два-пять - один гвоздь, два гвоздя, пять гвоздей.

Также PyTils реализует числа прописью

    >>> pytils.numeral.in_words(254)
    u'двести пятьдесят четыре'
    >>> pytils.numeral.in_words(2.01)
    u'две целых одна сотая'
    >>> pytils.numeral.rubles(2.01)
    u'два рубля одна копейка'
    >>> pytils.numeral.sum_string(32, pytils.numeral.MALE, (u"гвоздь", u"гвоздя", u"гвоздей"))
    u'тридцать два гвоздя'
    >>> pytils.numeral.sum_string(21, pytils.numeral.FEMALE, (u"белка", u"белки", u"белок"))
    u'двадцать одна белка'

Даты
----

В PyTils можно получить русские даты без использования локалей.

    >>> pytils.dt.ru_strftime(u"сегодня - %d %B %Y, %A", inflected=True)
    u'сегодня - 02 сентября 2006, суббота'

и получить величину периода:

    >>> pytils.dt.distance_of_time_in_words(time.time()-10000)
    u'2 часа назад'
    >>> pytils.dt.distance_of_time_in_words(time.time()+10000, accuracy=2)
    u'через 2 часа 46 минут'

Транслитерация
--------------

При помощи PyTils можно сделать транслитерацию:

    >>> print pytils.translit.translify(u"Проверка связи")
    'Proverka svyazi'
    >>> pytils.translit.detranslify("Proverka svyazi")
    u'Проверка связи'

В translify вывод - str, а не unicode. В detranslify вход может быть как 
unicode, так и str.

И сделать строку для URL (удаляются лишние символы, пробелы заменяются на 
дефисы):

    >>> pytils.translit.slugify(u"тест и еще раз тест")
    'test-i-esche-raz-test'

