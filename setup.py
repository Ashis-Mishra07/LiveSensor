from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements_list = []
    with open(file_path) as file_obj:
        requirements_list = file_obj.readlines()
        requirements_list = [req.replace("\n", "") for req in requirements_list]
    return requirements_list

setup(
    name='sensor',
    version='0.0.1',
    author='Ashis',
    author_email='mishralucky074@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # <-- pass the file here
)
