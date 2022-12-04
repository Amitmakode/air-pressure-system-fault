from setuptools import find_packages, setup

from typing import List
REQUIREMENT_FILE_NAME= "requirements.txt"

def get_requirements()->List[str]:...
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return    

setup(
    name = "sensor",
    version = "0.0.1",
    author = "ineuron",
    author_email = "amitmakode007@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),

)



 
#def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list

#setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="avnish@ineuron.ai",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)

