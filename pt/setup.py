from setuptools import setup, find_packages

setup(
    name='yourscript',
    version='0.1.0',
    packages=['pt'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'aa = pt.main:main',
        ],
    },
)
