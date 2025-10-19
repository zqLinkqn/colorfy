# setup.py
from setuptools import setup, find_packages

setup(
    name="colorfy",
    version="1.0.0",
    description="Библиотека для цветного текста в консоли",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="vvoid",
    author_email="plip30392@gmail.com",
    url="https://github.com/zqLinkqn/colorfy",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
