# Library to configure this setup file
from distutils.core import setup

# Import the version of the the pypsdier
from GenericSimulationLibrary import version as current_version
print("Current Library Version:", current_version)

# Use the README for the long description
long_description=open('README.rst').read() ### Change the content of README.rst

setup(
    name='GenericSimulationLibrary',        ### Change here
    version=current_version,
    author='Sebastian Flores Benner',       ### Change here
    author_email='sebastiandres@gmail.com', ### Change here
    packages=['GenericSimulationLibrary'],  ### Change here
    scripts=[],
    url='https://github.com/sebastiandres/GenericSimulationLibrary',    ### Change here
    license='MIT',  ### May/May not change this. But if you change it, must also change LICENCE file
    description='A simple but functional interface for simulation code.', ### Change here
    long_description=long_description,
)