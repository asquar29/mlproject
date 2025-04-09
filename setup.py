from setuptools import find_packages, setup



setup(
    name='mlproject',
    version='0.0.1',
    author='A Anand',
    author_email='mitochondria118@gmail.com'
    packages=find_packages()
    install_requires = get_requirements('requirements.txt')
)