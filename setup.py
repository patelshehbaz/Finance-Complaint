from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "finance-complaint"
VERSION = "0.0.1"
AUTHOR = "Shehbaz Patel"
DESCRIPTION = "This is a sample for an industry-ready solution"
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list(file_path=REQUIREMENT_FILE_NAME) -> List[str]:
    """
    Description: This function returns a list of requirements mentioned in the requirements.txt file.
    """
    try:
        with open(file_path) as requirement_file:
            requirement_list = [line.strip() for line in requirement_file if line.strip() and line.strip() != HYPHEN_E_DOT]
            return requirement_list
    except FileNotFoundError:
        print("The requirements file was not found.")
        return []

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
