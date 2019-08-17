from setuptools import setup



setup(
   name="test",
   version='1.0',
   py_module=['test'],
   install_requires=[
     'Click',
   ],
   entry_points='''
      [console_scripts]
      test= test:main
   ''',

)
