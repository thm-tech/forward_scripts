# -*- coding: utf-8 -*-
import os
import codecs

from setuptools import setup, find_packages


def read(*rnames):
    return codecs.open(os.path.join(os.path.dirname(__file__), *rnames), encoding='utf-8').read()


kwargs = {}
info = dict(
    name='forward_script',
    version='0.1',
    url='https://github.com/Mohanson/forward_script',
    license='PIL',
    author='Mohanson',
    author_email='mohanson@outlook.com',
    description='forward_script',
    long_description=read('README.md')
)
files = dict(
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'forward_script=forward_script.main:main',
        ]
    },
)

kwargs.update(info)
kwargs.update(files)
setup(
    zip_safe=False,
    install_requires=[],
    **kwargs
)