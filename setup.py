#!/usr/bin/env python
from setuptools import setup

version = "0.4.0"

setup(
    name='pytils',
    version=version,
    author='Yury Yurevich',
    author_email='yyurevich@jellycrystal.com',
    url='https://github.com/last-partizan/pytils/',
    description='Russian-specific string utils',
    long_description="""Simple tools for processing strings in russian
(choose proper form for plurals, in-words representation of numerals,
    dates in russian without locales, transliteration, etc)""",
    packages=[
        'pytils',
        'pytils.templatetags',
    ],
    license="MIT",
    platforms="All",
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: Russian',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
    ],
    zip_safe=True,
    test_suite='pytils.test.get_suite',
    include_package_data=True,
)
