from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    It removes any line that starts with '-' or is empty.
    """
    requirements = []
    HYPHEN_E_DOT = '-e .'

    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Abhinav Rai',
    author_email = 'raiabhinav.in@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)