from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ocpp',
    version='0.1.1',
    description="Python implementation of the Open Charge Point Protocol",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    install_requires=[
        'jsonschema (==3.0.1)',
    ],
    dependency_links=[],
    include_package_data=True,
)
