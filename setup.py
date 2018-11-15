from setuptools import setup, find_packages

print(find_packages(exclude=['tests']))

setup(
    name='classification_models',
    packages=find_packages(exclude=['tests']),
)
