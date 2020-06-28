from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mc4",
    version="1.0.0",
    author="Ayan Kumar Saha",
    author_email="ayankumarsaha96@gmail.com",
    description="A python package for implementing Markov Chain Type 4 rank aggregation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kalyaniuniversity/MC4",
    packages=find_packages(exclude=['docs', 'test*']),
    install_requires=['numpy>=1.19.0', 'pandas>=1.0.5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords='Machine Learning, Ranking, Markov Chain',
    python_requires='>=3.6',
    project_urls={  
        'Full Documentation': 'https://github.com/kalyaniuniversity/MC4/wiki',
        'Bug Reports': 'https://github.com/kalyaniuniversity/MC4/issues',
        'Follow Author': 'https://github.com/Ayan-Kumar-Saha'
    }
)
