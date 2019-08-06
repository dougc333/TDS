how to use click CLI tool

h1: create simple CLI wo using click. Use only setup.py. setup.py should be modified to support h1

from setuptools import setup
setup(
   name="hello",
   version='1.0',
   py_modules=['hello'],
   install_requires=[
     'Click',
   ],
   entry_points='''
      [console_scripts]
      h1=h1:cli
   ''',

)


def cli():
  print("some text")
>h1
some text

h2: simplest click, add click.command() which returns help menu. 

from setuptools import setup
setup(
   name="hello",
   version='1.0',
   py_modules=['hello'],
   install_requires=[
     'Click',
   ],
   entry_points='''
      [console_scripts]
      h2=h2:cli
   ''',
)



>h2 --help
