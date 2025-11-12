from setuptools import setup, find_packages

setup(
    name="test-python",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "pytest",
        "pytest-cov",
        "pytest-html",
        "flake8",
        "black",
    ],
)
