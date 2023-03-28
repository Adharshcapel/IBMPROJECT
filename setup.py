from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:  #  List[str] This will return a list, to recognize we import typing
    ''' 
    this function will return the list of requirements
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines() # Once we read  the line from inside requirement.txt one one line gets added so \n get added and we have to remove it
        requirement=[req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    
    return requirement

setup(
name='IBMATTRITIONCLASSIFICATION',
version='0.0.2',
author='Adharsh Sobhanan',
author_email='adharshsobhanan@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')

)
# In requirement.txt when we give -e . it will automaically tigger setp.py