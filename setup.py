import setuptools
import rdii

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rdii",
    version=rdii.__version__,
    author="Krzysztof Langner",
    author_email="klangner@gmail.com",
    description="Rainfall-Derived Infiltration and Inflow library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/klangner/rdii",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)