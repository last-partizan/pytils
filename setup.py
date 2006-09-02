#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
import os

import pytils

os.system("epydoc pytils")

setup(name='pytils',
      version=pytils.VERSION,
      author='Pythy',
      author_email='the.pythy@gmail.com',
      url='http://code.google.com/p/pythy/',
      description='Utils for easy processing string in russian.',
      long_description="""Simple tools for processing string in russian 
(choose proper form for plurals, in-words representation of numerals,
dates in russian without locales, transliteration, etc)""",
      download_url='http://pythy.googlecode.com/svn/trunk/pytils/',
      packages=['pytils', 'pytils.test'],
      license="GPL",
      platforms="All",
      classifiers = [
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Linguistic',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Natural Language :: Russian',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
        ],
     )
