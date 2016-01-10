from setuptools import setup, find_packages

setup(
    name = "Greengraph",
    version = "1.0",
    packages = find_packages(exclude=['*test']),
    author = "Padraic Calpin",
    author_email = "padraic.calpin93@gmail.com",
    license = "GPLv2",
    scripts = ['scripts/greengraph'],
    install_requires = ['requests','numpy','matplotlib','geopy'],
    setup_requires = ['nose'],
    test_suite = 'nose.collector')