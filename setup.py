import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

with open('yahoofantasy/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


setuptools.setup(
    name="pointofvue",
    version=version,
    author="Matt Dodge",
    author_email="mattedgod@gmail.com",
    description="A simple, opinionated way to incorporate VueJS into Django apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=reqs,
    data_files=[
        'templates',
    ],
    url="https://github.com/mattdodge/PointOfVue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
