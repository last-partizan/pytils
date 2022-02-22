# -*- coding: utf-8 -*-

import datetime
import sys
import time

from django import VERSION as _django_version
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic.base import TemplateView

from pytils import VERSION as pytils_version


def get_python_version():
    return '.'.join(str(v) for v in sys.version_info[:3])


def get_django_version(_ver):
    ver = '.'.join([str(x) for x in _ver[:-2]])
    return ver


class DtView(TemplateView):
    template_name = 'dt.html'

    def get_context_data(self, **kwargs):
        context = super(DtView, self).get_context_data(**kwargs)
        context.update({
          'ctime': time.time(),
          'otime': time.time() - 100000,
          'ftime': time.time() + 100000,
          'cdate': datetime.datetime.now(),
          'odate': datetime.datetime.now() - datetime.timedelta(0, 100000),
          'fdate': datetime.datetime.now() + datetime.timedelta(0, 100000),
         })
        return context


class NumeralView(TemplateView):
    template_name = 'numeral.html'

    def get_context_data(self, **kwargs):
        context = super(NumeralView, self).get_context_data(**kwargs)
        context.update({
          'comment_variants': ('комментарий', 'комментария', 'комментариев'),
          'comment_number': 21,
          'zero': 0,
          'comment_gender': 'MALE',
          'rubles_value': 23.152,
          'rubles_value2': 12,
          'int_value': 21,
          'float_value': 31.385,
        })
        return context


class TranslitView(TemplateView):
    template_name = 'translit.html'

    def get_context_data(self, **kwargs):
        context = super(TranslitView, self).get_context_data(**kwargs)
        context.update({
          'text': 'Пример траслитерации средствами pytils',
          'translit': 'Primer obratnoj transliteratsii',
        })
        return context


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
          'pytils_version': pytils_version,
          'django_version': get_django_version(_django_version),
          'python_version': get_python_version(),
        })
        return context


urlpatterns = [
    path('dt/', DtView.as_view(), name='pytils_dt_example'),
    path('numeral/', NumeralView.as_view(), name='pytils_numeral_example'),
    path('translit/', TranslitView.as_view(), name='pytils_translit_example'),
    path('', IndexView.as_view(), name='pytils_example'),
]

urlpatterns += staticfiles_urlpatterns()
