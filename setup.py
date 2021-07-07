#!/usr/bin/env python3
from setuptools import setup, find_packages
from io import open

# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(name='wifihunter',
      version='1.0.0',
      description='WiFi Penetration Toolkit',
      long_description=read('README.rst'),
      long_description_content_type="text/x-rst",
      author='Mustafa Asaad',
      author_email='ma24th@yahoo.com',
      url='https://github.com/MA24th/WiFiHunter',

      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'wifihunter = wifihunter.__main__:start'
              ]},
      scripts=['bin/wifihunter'],
      data_files=[
          ('share/dict', ['wordlist-top4800-probable.txt'])
      ],
      include_package_data=True,
      exclude_package_data={"": ["README.md"]},
      
    #   install_requires=[
          
    #   ],
      test_suite='pytest',
      tests_require=['pytest'],

      license='GNU GPLv2',
      keywords='wifi penetration toolkit',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      ],
      )
