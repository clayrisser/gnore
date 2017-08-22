from setuptools import setup, find_packages
from codecs import open
from os import path
from gnore import config

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = list()
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    for line in f.readlines():
        install_requires.append(line)

setup(
    name=config.NAME,

    version=config.VERSION,

    description='Utility for .gitignore',

    long_description=long_description,

    url='https://github.com/jamrizzi/gnore',

    author='Jam Risser',

    author_email='jam@jamrizzi.com',

    license='MIT',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='cli git github clean ignore gitignore command line',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=install_requires,

    entry_points = {
        'console_scripts': [config.NAME + '=' + config.NAME + '.__main__:main'],
    }
)
