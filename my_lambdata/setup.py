
# setup.py file
## helps you specify the metadata

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-DSPT5sean", # the name that you will install via pip
    version="1.6",
    author="Sean",
    author_email="your@email.com",
    description="a package created for training purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/ssbyrne89/lambdata-DSPT5sean",
    #keywords="",
    packages=["my_lambdata"] # ["my_lambdata"]
)