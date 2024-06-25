from setuptools import setup, find_packages

setup(
    name="sparky_utils",
    version="1.0.1",
    author="Ayobami Alaran",
    author_email="ayobamidele006@gmail.com",
    description="Python and Django Project Utils Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ayobami6/sparky_utils",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "asgiref==3.8.1",
        "Django==4.2.13",
        "djangorestframework==3.15.1",
    ],
)
