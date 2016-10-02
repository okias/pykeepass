from distutils.core import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pykeepass',
    version='1.2',
    license='GPL3',
    description='Low-level library to interact with keepass databases '\
                '(supports the v.4 format)',
    long_description=read('README.rst'),
    author='Philipp Schmitt',
    author_email='philipp@schmitt.co',
    url='https://github.com/pschmitt/pykeepass',
    packages=['pykeepass'],
    install_requires=['libkeepass-unicode'],
    entry_points={
        'console_scripts': ['pkpwrite=pykeepass.pkpwrite:main']
    }
)
