#!/usr/bin/env python

import sys
import glob
import os.path
import numpy

import setuptools
from setuptools import setup, Extension
from distutils.command.install_data import install_data

datafiles = [os.path.basename(x) for x in glob.glob('tests/*.fits')]

setup(
    name = 'pyfits',
    version = '3.5.1',
    python_requires='>=3.3',
    author = (
        'J. C. Hsu, Paul Barrett, Christopher Hanley, James Taylor, '
        'Michael Droettboo'
    ),

    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    packages = [
        'pyfits',
        'pyfits._compat',
        'pyfits._compat._odict_py2',
        'pyfits._compat._weakset_py2',
        'pyfits.extern',
        'pyfits.hdu',
        'pyfits.scripts',
        'pyfits.tests',
    ],

    data_files = [
        ('tests', datafiles),
    ],

    ext_modules = [
        Extension(
            'pyfits.compression',
            glob.glob('cextern/cfitsio/*.c') + glob.glob('src/*.c'),
            language='c',
            include_dirs=[
                'cextern/cfitsio',
                numpy.get_include(),
            ]
        ),
    ],

    install_requires=['numpy'],
)
