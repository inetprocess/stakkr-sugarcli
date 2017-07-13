from setuptools import setup

setup(
    name='MarinaSugarCLI',
    version='1.0',
    packages=['sugarcli'],
    entry_points='''
        [marina.plugins]
        sugarcli=sugarcli.core:sugarcli
    '''
)
