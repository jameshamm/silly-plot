from setuptools import setup

setup(
    name="sillyploy",
    version="0.1",
    description="Plot real-time data",
    url="http://github.com/jameshamm/silly-plot",
    author="James Hamm",
    packages=["sillyplot"],
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    scripts=['bin/silly-plot'])
