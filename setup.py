from codecs import open
from setuptools import setup, find_packages

NAME = 'concierge'
VERSION = "0.0.3"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = []

setup(
    name=NAME,
    version=VERSION,
    description='Concierge',
    long_description='Create a sample Azure DevOps project and Azure resources in a single command.',
    license='MIT',
    author='E-gineering',
    author_email='robbie.page@e-gineering.com',
    url='https://github.com/egineering-llc/Concierge',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES
)
