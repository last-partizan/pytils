# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from pytils import VERSION as pytils_version


class ExamplesTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def testIndex(self):
        resp = self.c.get(reverse('pytils_example'))
        self.assertEqual(resp.status_code, 200)
        body = resp.content.decode('utf-8')
        self.assertTrue('pytils %s' % pytils_version in body)
        self.assertTrue(reverse('pytils_dt_example') in body)
        self.assertTrue(reverse('pytils_numeral_example') in body)
        self.assertTrue(reverse('pytils_translit_example') in body)

    def testDt(self):
        resp = self.c.get(reverse('pytils_dt_example'))
        self.assertEqual(resp.status_code, 200)
        body = resp.content.decode('utf-8')
        self.assertTrue('distance_of_time' in body)
        self.assertTrue('ru_strftime' in body)
        self.assertTrue('ru_strftime_inflected' in body)
        self.assertTrue('ru_strftime_preposition' in body)
        self.assertTrue('вчера' in body)
        self.assertTrue('завтра' in body)

    def testNumeral(self):
        resp = self.c.get(reverse('pytils_numeral_example'))
        self.assertEqual(resp.status_code, 200)
        body = resp.content.decode('utf-8')
        self.assertTrue('choose_plural' in body)
        self.assertTrue('get_plural' in body)
        self.assertTrue('rubles' in body)
        self.assertTrue('in_words' in body)
        self.assertTrue('sum_string' in body)
        self.assertTrue('комментарий' in body)
        self.assertTrue('без примеров' in body)
        self.assertTrue('двадцать три рубля пятнадцать копеек' in body)
        self.assertTrue('двенадцать рублей' in body)
        self.assertTrue('двадцать один' in body)
        self.assertTrue('тридцать одна целая триста восемьдесят пять тысячных' in body)
        self.assertTrue('двадцать один комментарий' in body)

    def testTranslit(self):
        resp = self.c.get(reverse('pytils_translit_example'))
        self.assertEqual(resp.status_code, 200)
        body = resp.content.decode('utf-8')
        self.assertTrue('translify' in body)
        self.assertTrue('detranslify' in body)
        self.assertTrue('slugify' in body)
        self.assertTrue('Primer trasliteratsii sredstvami pytils' in body)
        self.assertTrue('primer-trasliteratsii-sredstvami-pytils' in body)
        self.assertTrue('primer-obratnoj-transliteratsii' in body)
