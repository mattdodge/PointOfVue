import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

reqs = [
]

setuptools.setup(
    name="pointofvue",
    version="0.0.1",
    author="Matt Dodge",
    author_email="mattedgod@gmail.com",
    description="A simple, opinionated way to incorporate VueJS into Django apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=reqs,
    url="https://github.com/mattdodge/PointOfVue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
