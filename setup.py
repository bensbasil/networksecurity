'''
The setup.py is an essential part of packaging and 
distributing python projects. It's used by setuptools to define the configuration
of your project, such as its metadata, dependencies and more 
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst = [] # Initialized to fix the NameError
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            ## Process each lines
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and the editable flag (-e .)
                if requirement and not requirement.startswith('-e'):
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Bens Basil",
    author_email="bensdbasil@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)
