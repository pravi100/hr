from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='manage users on a server based on an inventory JSON file',
    long_description=readme,
    author='praveen',
    author_email='praveenchigurupati2012@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
