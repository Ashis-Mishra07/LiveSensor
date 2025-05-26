from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements_list : list[str] = []
    return requirements_list


setup(
    name='sensor',
    version='0.0.1',
    author='Ashis',
    author_email='mishralucky074@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)