import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MC4", # Replace with your own username
    version="0.0.1",
    author="Ayan Kumar Saha",
    author_email="ayankumarsaha96@gmail.com",
    description="A package for implementing Markov Chain Type 4 rank aggregation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Publice Licence version 3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)