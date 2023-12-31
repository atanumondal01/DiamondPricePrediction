#setup is there so that we can import to other 
from setuptools import find_packages,setup
from typing import List
hypen="-e ."
def get_requirements(file_path:str)->List[str]:
   requirements=[]
   #file_path is requi.txt
   with open(file_path) as file_obj:
      requirements=file_obj.readlines()
      requirements=[req.replace("/n","") for req in requirements]
      
      #if hypen in requirements: 
       #  requirements.remove(hypen)
   return requirements

setup(
   name="DiamondPricePrediction",
   version="0.0.1",#we can update the version when we release the updated code
   author="Atanu Mondal",
   author_email="atanum390@gmail.com",
   install_requires=get_requirements("requirements.txt"),#all these in requi.txt
   packages=find_packages()

)