from setuptools import find_packages,setup
def get_requirements(file_path:str):
    requirment=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if "-e ." in requirments:
            requirments.remove("-e .")
    return requirments
setup(

    name="NLP Text summarizar project",
    author_email='sk0551460@gamil.com',
    version="0.0.02",
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')
)