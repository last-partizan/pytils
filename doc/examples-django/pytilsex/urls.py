# -*- coding: utf-8 -*-

import time
import datetime

from django.conf.urls.defaults import *
import settings

from pytils import VERSION as pytils_version
from django import VERSION as _django_version

def get_django_version(_ver):
    suffix = _ver[-1]
    ver = '.'.join([str(x) for x in _ver[:-1]])
    if suffix is not None:
        ver += suffix
    return ver

urlpatterns = patterns('django.views',
    (r'^dt/', 'generic.simple.direct_to_template',
         {'template': 'dt.html',
          'ctime': time.time(),
          'otime': time.time() - 100000,
          'ftime': time.time() + 100000,
          'cdate': datetime.datetime.now(),
          'odate': datetime.datetime.now() - datetime.timedelta(0, 100000),
          'fdate': datetime.datetime.now() + datetime.timedelta(0, 100000),
          }   
    ),
    (r'^numeral/', 'generic.simple.direct_to_template',
         {'template': 'numeral.html',
          'comment_variants': ('комментарий', 'комментария', 'комментариев'),
          'comment_number': 21,
          'zero': 0,
          'comment_gender': 'MALE',
          'rubles_value': 23.152,
          'rubles_value2': 12,
          'int_value': 21,
          'float_value': 31.385,
          }   
    ),
    (r'^translit/', 'generic.simple.direct_to_template',
         {'template': 'translit.html',
          'text': 'Пример траслитерации средствами pytils',
          'translit': 'Primer obratnoj transliteratsii',
          }   
    ),

    (r'^static/(?P<path>.*)$', 'static.serve',
         {'document_root': settings.MEDIA_ROOT,
          }   
    ),
    
    (r'^$', 'generic.simple.direct_to_template',
        {'template': 'base.html',
         'pytils_version': pytils_version,
          'django_version': get_django_version(_django_version)}
    ),
)
