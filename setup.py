# coding=utf-8
from setuptools import setup

setup(
    name='irclib',
    version='0.1.0',
    python_requires=">=3.3",
    description="A simple library for working with the IRC protocol",
    url='https://github.com/snoonetIRC/irclib',
    author='linuxdaemon',
    author_email='linuxdaemon@snoonet.org',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='irc irc-parser',
    packages=['irclib'],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)