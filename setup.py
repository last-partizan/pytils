#!/usr/bin/env python
# -*- coding: utf-8 -*-

use_setuptools = True
if use_setuptools:
    try:
        from setuptools import setup
    except ImportError:
        print "Cannot load setuptool, revert to distutils"
        use_setuptools = False
        from distutils.core import setup
else:
    from distutils.core import setup

version = "0.2.3"

setup_data = {
      'name': 'pytils',
      'version': version,
      'author': 'Yury Yurevich',
      'author_email': 'the.pythy@gmail.com',
      'url': 'http://www.pyobject.ru/projects/pytils/',
      'description': 'Russian-specific string utils',
      'long_description': """Simple tools for processing strings in russian
(choose proper form for plurals, in-words representation of numerals,
dates in russian without locales, transliteration, etc)""",
      'packages': ['pytils', 'pytils.templatetags', 'pytils.test', 'pytils.test.templatetags', 'pytils.third'],
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
