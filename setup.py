from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ocpp',
    version='0.1.0',
    description="Python implementation of the Open Charge Point Protocol",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),  # Required
    install_requires=[
        'jsonschema (==2.6.0)',
    ],
    dependency_links=[],  # Optional
    include_package_data=True,
)
