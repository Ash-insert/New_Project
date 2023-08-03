from setuptools import find_packages, setup


def get_requirements(file_path:str) -> list:
    """
    This function will return requirements
    """

    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        # \n gets added after reading each line
        requirements = [ req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'New ML project',
    version = '0.0.1',
    author = 'Aniket Hinge',
    author_email= 'ahinge1999@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)