import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    #'psycopg2',
    #'cx_Oracle',
    'SQLAlchemy',    
    ]

setup(name='mabo',
      version='0.0.1',
      description='mabo',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: ",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='MaboTech',
      license='MIT',
      author_email='mabotech@163.com',
      url='http://www.mabotech.com',
      keywords='mabotech mabo lib',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='maboss',
      install_requires = requires
  )

