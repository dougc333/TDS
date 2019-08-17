from setuptools import setup

setup(
    name='y',
    version='0.1',
    py_modules=['y'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        y=y:main
    ''',
)
