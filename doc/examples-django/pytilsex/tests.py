# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from pytils import VERSION as pytils_version

class ExamplesTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def testIndex(self):
        resp = self.c.get(reverse('pytils_example'))
        self.assertEquals(resp.status_code, 200)
        self.assert_('pytils %s' % pytils_version in resp.content)
        self.assert_(reverse('pytils_dt_example') in resp.content)
        self.assert_(reverse('pytils_numeral_example') in resp.content)
        self.assert_(reverse('pytils_translit_example') in resp.content)

    def testDt(self):
        resp = self.c.get(reverse('pytils_dt_example'))
        self.assertEquals(resp.status_code, 200)
        self.assert_('distance_of_time' in resp.content)
        self.assert_('ru_strftime' in resp.content)
        self.assert_('ru_strftime_inflected' in resp.content)
        self.assert_('ru_strftime_preposition' in resp.content)
        self.assert_('вчера' in resp.content)
        self.assert_('завтра' in resp.content)

    def testNumeral(self):
        resp = self.c.get(reverse('pytils_numeral_example'))
        self.assertEquals(resp.status_code, 200)
        self.assert_('choose_plural' in resp.content)
        self.assert_('get_plural' in resp.content)
        self.assert_('rubles' in resp.content)
        self.assert_('in_words' in resp.content)
        self.assert_('sum_string' in resp.content)
        self.assert_('комментарий' in resp.content)
        self.assert_('без примеров' in resp.content)
        self.assert_('двадцать три рубля пятнадцать копеек' in resp.content)
        self.assert_('двенадцать рублей' in resp.content)
        self.assert_('двадцать один' in resp.content)
        self.assert_('тридцать одна целая триста восемьдесят пять тысячных' in resp.content)
        self.assert_('двадцать один комментарий' in resp.content)

    def testTranslit(self):
        resp = self.c.get(reverse('pytils_translit_example'))
        self.assertEquals(resp.status_code, 200)
        self.assert_('translify' in resp.content)
        self.assert_('detranslify' in resp.content)
        self.assert_('slugify' in resp.content)
        self.assert_('Primer trasliteratsii sredstvami pytils' in resp.content)
        self.assert_('primer-trasliteratsii-sredstvami-pytils' in resp.content)
        self.assert_('primer-obratnoj-transliteratsii' in resp.content)