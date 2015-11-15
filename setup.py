from distutils.core import setup
from setuptools import setup, find_packages

setup( name='django_test',
    version='0.1',
    description='Just test',
    author='Stas Kridzanovskiy',
    author_email='slaviann@gmail.com',
    packages=find_packages(),
      install_requires=[
          'Django==1.8.6 ',
      ],
    )
