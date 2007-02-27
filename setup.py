#!/usr/bin/env python
# -*- coding: utf-8 -*-

use_setuptools = True
try:
    from setuptools import setup
except ImportError:
    use_setuptools = False
    from distutils.core import setup

import pytils

rel_download_url = "http://pythy.googlecode.com/svn/tags/pytils/%s/dist/"
tag_version = pytils.VERSION.replace('.', '_')

setup_data = {
      'name': 'pytils',
      'version': pytils.VERSION,
      'author': 'Yury Yurevich',
      'author_email': 'the.pythy@gmail.com',
      'url': 'http://gorod-omsk.ru/blog/pythy/projects/pytils/',
      'description': 'Utils for easy processing string in russian.',
      'long_description': """Simple tools for processing string in russian 
(choose proper form for plurals, in-words representation of numerals,
dates in russian without locales, transliteration, etc)""",
      'download_url': rel_download_url % tag_version,
      'packages': ['pytils', 'pytils.templatetags', 'pytils.test', 'pytils.test.templatetags'],
      'license': "GPL",
      'platforms': "All",
      'classifiers': [
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Linguistic',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Natural Language :: Russian',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
        ],
    }
setuptools_extensions = {
    'zip_safe': True,
    'test_suite': 'pytils.test.get_suite',
    'include_package_data': True,
    }

if use_setuptools:
    setup_data.update(setuptools_extensions)

args = ()
kwargs = setup_data
setup(*args, **kwargs)
