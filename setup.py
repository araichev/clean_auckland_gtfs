from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='clean_auckland_gtfs',
    version='0.1.0',
    description='Python 3.5+ tools for cleaning Auckland Transport GTFS feeds',
    long_description=readme,
    author='Alex Raichev',
    author_email='alex@raichev.net',
    url='https://github.com/araichev/clean_auckland_gtfs',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    install_requires=[
        'gtfstk>=6.1.0',
    ],
)
