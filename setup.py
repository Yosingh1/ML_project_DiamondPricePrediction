from setuptools import setup , find_packages

def get_requirements(path_file):
    HYPE_E_DOT = "-e ."
    requirements =[]
    with open(path_file) as file_obj:
        requirements = file_obj.readlines()

        requirements = [req.replace("\n","") for req in requirements]

        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    return requirements


setup(name="regression_model",
      version="0.0.01",
      author="yogendra",
      author_email="globaldspvt@gmail.com",
      install_requires=get_requirements("requirements.txt"),
      packages=find_packages(),
      )