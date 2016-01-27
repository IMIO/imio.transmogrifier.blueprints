# -*- coding: utf-8 -*-
"""Installer for the imio.transmogrifier.blueprints package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read() +
    '\n' +
    'Contributors\n' +
    '============\n' +
    '\n' +
    open('CONTRIBUTORS.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')


setup(
    name='imio.transmogrifier.blueprints',
    version='1.0a1',
    description="Groups and deploy all differents blueprints to migrate Imio Plone Site 2.x, 3.x to Plone 4.x. (read import.cfg)",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='boulch',
    author_email='christophe.boulanger@imio.be',
    url='https://pypi.python.org/pypi/imio.transmogrifier.blueprints',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imio', 'imio.transmogrifier'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'collective.transmogrifier',
        'plone.app.transmogrifier',
        'quintagroup.transmogrifier',
        'imio.transmogrifier.cardimporter',
        'imio.transmogrifier.PloneFormGen',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
