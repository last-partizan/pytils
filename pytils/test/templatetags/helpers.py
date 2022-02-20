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
    def check_template_tag(self, template_name, template_string, context, result_string):
        """
        Method validates output of template tag or filter
        
        @param template_name: name of template
        @type template_name: C{str}
        
        @param template_string: contents of template
        @type template_string: C{str} or C{unicode}

        @param context: rendering context
        @type context: C{dict}

        @param result_string: reference output
        @type result_string: C{str} or C{unicode}
        """
        t = Template(template_string)
        c = Context(context)
        output = t.render(c)
        self.assertEquals(output, result_string)

