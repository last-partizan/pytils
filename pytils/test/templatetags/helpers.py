# -*- coding: utf-8 -*-
"""
Helpers for templatetags' unit tests in Django webframework
"""
from django.template import Context, Template
from django.test import TestCase


class TemplateTagTestCase(TestCase):
    """
    TestCase for testing template tags and filters
    """
    def check_template_tag(self, template_string: str, context: dict, result_string: str) -> None:
        """
        Method validates output of template tag or filter

        @rtype: object
        @param template_string: contents of template
        @type template_string: C{str}

        @param context: rendering context
        @type context: C{dict}

        @param result_string: reference output
        @type result_string: C{str}
        """
        t = Template(template_string)
        c = Context(context)
        output = t.render(c)
        self.assertEqual(output, result_string)

