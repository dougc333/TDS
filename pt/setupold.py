import setuptools
import os

DIR = os.path.dirname(__file__)
REQUIREMENTS = os.path.join(DIR, "requirements.txt")

with open(REQUIREMENTS) as f:
    reqs = f.read()

#entry_points={"console_scripts": ["pt = pt.main:main"]},
setuptools.setup(
    name="pt",
    version="0.1",
    description="test project",
    url="https://github.com/dougc333/pt",
    author="dc",
    license="BSD",
    packages=setuptools.find_packages(),
    install_requires=reqs.strip().split("\n"),
    entry_points={"console_scripts": ["pt = pt.pt:main"]},
)
