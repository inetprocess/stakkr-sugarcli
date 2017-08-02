from setuptools import setup

setup(
    name='StakkrSugarCLI',
    version='3.2',
    packages=['sugarcli'],
    entry_points='''
        [stakkr.plugins]
        sugarcli=sugarcli.core:sugarcli
    '''
)
