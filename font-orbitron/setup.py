#!/usr/bin/env python

"""
MIT License

Copyright (c) 2020 Juan Castro Fernández

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Text Processing :: Fonts']

setup(
    name            = 'font-orbitron',
    version         = '0.0.1',
    author          = 'Juan Castro Fernández',
    author_email    = 'hola@juancastro.es',
    description     = 'Orbitron font',
    long_description= open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
    license         = 'SIL OFL 1.1',
    keywords        = 'Kaushan Script Font',
    url             = 'https://github.com/castrofernandez/fonts-python',
    classifiers     = classifiers,
    py_modules      = [],
    packages        = ['font_orbitron'],
    package_data    = {'font_orbitron': ['font_orbitron/files']},
    entry_points    = {
        'fonts_ttf': [
            'font-orbitron = font_orbitron:font_files'
        ]
    },
    zip_safe        = False,
    include_package_data = True
)
