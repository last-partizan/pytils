# -*- coding: utf-8 -*-

import time
import datetime

from django.conf.urls.defaults import *

urlpatterns = patterns('django.views.generic.simple',
    (r'^dt/', 'direct_to_template',
         {'template': 'dt.html',
          'ctime': time.time(),
          'otime': time.time() - 100000,
          'ftime': time.time() + 100000,
          'cdate': datetime.datetime.now(),
          }   
    ),
    (r'^numeral/', 'direct_to_template',
         {'template': 'numeral.html',
          'comment_variants': ('комментарий', 'комментария', 'комментариев'),
          'comment_number': 21,
          'comment_gender': 1,
          'rubles_value': 23.1,
          'rubles_value2': 12,
          'int_value': 21,
          'float_value': 31.385,
          }   
    ),
    (r'^translit/', 'direct_to_template',
         {'template': 'translit.html',
          'text': 'Пример траслитерации средствами PyTils',
          'translit': 'Primer obratnoj transliteratsii',
          }   
    ),
    
    (r'^$', 'direct_to_template',
        {'template': 'base.html'}
    ),
)
