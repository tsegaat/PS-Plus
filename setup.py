from setuptools import find_packages, setup

with open("README.md") as f:
    content = f.read()

setup(
    name="Playstation",
    packages=find_packages(),
    version="0.1.0",
    long_description=content,
    description="Playstation libary to give you easy access to what you can do with your playstation",
    author="Tsega Amanuel",
    license="MIT LICENSE",
    install_requires=[],
)
