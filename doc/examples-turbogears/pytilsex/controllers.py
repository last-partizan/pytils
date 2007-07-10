# -*- coding: utf-8 -*-
import logging
import time
import datetime
import cherrypy
import turbogears
import pkg_resources

from turbogears import controllers, expose, validate, redirect
from pytils import numeral, VERSION as pytils_version

log = logging.getLogger("pytilsex.controllers")

def get_tg_version():
    try:
        ver = pkg_resources.get_distribution('TurboGears')._version
    except AttributeError:
        # setuptools 0.6c5
        ver = pkg_resources.get_distribution('TurboGears').version
    return ver

class Root(controllers.RootController):
    @expose(template="pytilsex.templates.root")
    def index(self):
        log.debug("pytilsex root controller ready to go")
        return {
            'tg_version': get_tg_version(),
            'pytils_version': pytils_version,
        }

    @expose(template="pytilsex.templates.dt")
    def dt(self):
        log.debug("pytilsex root/dt controller ready to go")
        return {
            'otime': time.time()-100000,
            'ftime': time.time()+100000,
            'odate': datetime.datetime.now() - datetime.timedelta(0,100000),
            'fdate': datetime.datetime.now() + datetime.timedelta(0,100000),
            }

    @expose(template="pytilsex.templates.numeral")
    def numeral(self):
        log.debug("pytilsex root/numeral controller ready to go")
        return {
            'comment_variants': (u"комментарий", u"комментария", u"комментариев"),
            'comment_number': 21,
            'zero': 0,
            'comment_gender': numeral.MALE,
            'rubles_value': 23.152,
            'rubles_value2': 12,
            'int_value': 21,
            'float_value': 31.385,
            }
        
    @expose(template="pytilsex.templates.translit")
    def translit(self):
        log.debug("pytilsex root/translit controller ready to go")
        return {
            'text': u'Пример транслитерации средствами pytils',
            'translit': 'Primer obratnoj transliteratsii',
            }
