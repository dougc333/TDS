import os,setuptools 


setuptools.setup(
    name="test",
    version="0.1",
    description="test",
    author="ghost",
    entry_points={"console_scripts": ["testme = main:main"]},
)