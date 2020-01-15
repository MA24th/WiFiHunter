from setuptools import setup
from io import open

# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(name='wifihunter',
      version='1.0.0',
      description='WiFi Penetration ToolKit',
      long_description=read('README.rst'),
      long_description_content_type="text/x-rst",
      author='Mustafa Asaad',
      author_email='ma24th@yahoo.com',
      url='https://github.com/MA24th/WiFiHunter',
      packages=['wifihunter'],
      license='GPLv2',
      keywords='wifi penetration toolkit',
      #   install_requires=[],
      #   extras_require={},
      classifiers=[
          'Programming Language :: Python :: 3',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
      ]
      )
