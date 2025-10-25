# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md', encoding="utf8") as f:
    readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='calculator',
    version='0.1.0',
    description='Simple Calculator that can also calculate words from 0-9 in a few languages',
    long_description=readme,
    author='Ramez Chreide',
    author_email='me@ramezchreide.com',
    url='https://github.com/RamezCh/BHT/tree/main/Computer%20Science%20for%20Data%20Science/calculator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)