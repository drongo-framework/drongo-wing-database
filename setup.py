#!/usr/bin/env python

from setuptools import find_packages, setup


VERSION = '1.2.0'
REPO_URL = 'https://github.com/drongo-framework/drongo-wing-database'

setup(
    name='drongo-wing-database',
    version=VERSION,
    description='Drongo wing database module.',
    author='Sattvik Chakravarthy, Sagar Chakravarthy',
    author_email='sattvik@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'drongo-wing-module>=1.2.0',
    ],
    packages=find_packages(),
    url=REPO_URL,
    include_package_data=True,
    zip_safe=False,
)
