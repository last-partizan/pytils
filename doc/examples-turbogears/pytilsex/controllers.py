# -*- coding: utf-8 -*-
import logging
import time
import cherrypy
import turbogears

from turbogears import controllers, expose, validate, redirect

log = logging.getLogger("pytilsex.controllers")

class Root(controllers.RootController):
    @expose(template="pytilsex.templates.root")
    def index(self):
        log.debug("pytilsex root controller ready to go")
        return {}

    @expose(template="pytilsex.templates.dt")
    def dt(self):
        log.debug("pytilsex root/dt controller ready to go")
        return {
            'otime': time.time()-100000,
            'ftime': time.time()+100000,
            }

    @expose(template="pytilsex.templates.numeral")
    def numeral(self):
        log.debug("pytilsex root/numeral controller ready to go")
        return {
            'comment_variants': (u"комментарий", u"комментария", u"комментариев"),
            'comment_number': 21,
            'comment_gender': 1,
            'rubles_value': 23.152,
            'rubles_value2': 12,
            'int_value': 21,
            'float_value': 31.385,
            }
        
    @expose(template="pytilsex.templates.translit")
    def translit(self):
        log.debug("pytilsex root/translit controller ready to go")
        return {
            'text': u'Пример транслитерации средствами PyTils',
            'translit': 'Primer obratnoj transliteratsii',
            }
