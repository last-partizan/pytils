from django.conf import settings

settings.configure(
    TEMPLATE_DIRS=(),
    TEMPLATE_CONTEXT_PROCESSORS=(),
    TEMPLATE_LOADERS=(),
    INSTALLED_APPS=('pytils',),
)

from django import template
from django.template import loader

import unittest


class TemplateTagTestCase(unittest.TestCase):
    
    def check_template_tag(self, template_name, template_string, context, result_string):
        
        def test_template_loader(template_name, template_dirs=None):
            return template_string, template_name
        
        loader.template_source_loaders = [test_template_loader,]
        
        output = loader.get_template(template_name).render(template.Context(context))
        
        self.assertEquals(output, result_string)
