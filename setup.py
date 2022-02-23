#!/usr/bin/env python
from setuptools import setup

version = "0.4.1"

setup(
    name='pytils',
    version=version,
    author='Yury Yurevich',
    author_email='yyurevich@jellycrystal.com',
    url='https://github.com/last-partizan/pytils/',
    description='Russian-specific string utils',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
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
    include_package_data=True,
)
