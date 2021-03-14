#!/usr/bin/env python

from distutils.core import setup


setup(
    name='unittest-or-fail',
    version='0',
    description='Run unittests or fail if no tests were found',
    author='Michał Górny',
    author_email='mgorny@gentoo.org',
    url='https://github.com/mgorny/unittest-or-fail',
    py_modules=['unittest_or_fail'],
    license='2-clause BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
