from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="betterText",
    version="0.0.1",
    description="Modify text in fun ways in the python terminal. Great for command line/text games.",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Burndowntheworld",
    author_email="burndowntheworld1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["colorama>=0.4.4","typing>=3.7.4.3"],
    python_requires=">=3.10",
)