from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="flipkart-product-recommender",
    version="0.1",
    author="Sheikh Noushad",
    packages=find_packages(),
    install_requires=requirements,
)
