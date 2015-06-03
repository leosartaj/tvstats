#!/usr/bin/env python2

from tvstats import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = 'tvstats',
    version = __version__,
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Scrape data of all the episodes of a Tv Series from IMDB'),
    long_description = open('README.rst').read() + '\n\n' + \
    open('CHANGELOG.rst').read(),
    license = 'MIT',
    keywords = 'tv tvseries series IMBD scrape crawl',
    url = 'http://github.com/leosartaj/tvstats',
    packages=find_packages(),
    scripts=['bin/tvstats'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
