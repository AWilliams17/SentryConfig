from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='SentryConfig',
    version='1.0.1',
    description='Lightweight project configuration management/parsing package.',
    long_description="For more information, see https://github.com/AWilliams17/SentryConfig/README.md",
    url='https://github.com/AWilliams17/SentryConfig/',
    author='Austin Williams',
    author_email='awilliams17412@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Topic :: Other/Nonlisted Topic',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='config configuration configuration-manager',
    packages=['sentryconfig'],

    project_urls={
        'Bug Reports': 'https://github.com/AWilliams17/SentryConfig/issues',
        'Source': 'https://github.com/AWilliams17/SentryConfig/'
    }, install_requires=['pytest']
)
