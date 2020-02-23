""" schemaverse_dojo packaging instructions """

from setuptools import setup, find_packages

setup(
    name='schemaverse_dojo',
    packages=['schemaverse_dojo'],
    version='0.1',
    description='Rapid deployment tool for Schemaverse,'
    author='FrozenFOXX',
    author_email='frozenfoxx@churchoffoxx.net',
    url='https://github.com/frozenfoxx/schemaverse_dojo',
    download_url='https://github.com/frozenfoxx/schemaverse_dojo/archive/0.1.tar.gz',
    keywords=['schemaverse','docker'],
    classifiers=[],
    install_requires=[
        'docker'
    ],
    scripts=[
        'scripts/schemaverse_dojo',
    ],
    data_files=[
        ('/etc/schemaverse_dojo', ['conf/dojo.conf', 'conf/players.conf'])
    ],
)
