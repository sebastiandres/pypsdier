Installation
====================

The repository for the code is hosted at `<https://github.com/sebastiandres/GenericSimulationLibrary>`_.

The current implementation has been developed in Python 3. 

To use it the simulation code, you should consider using the standard libraries numpy and matplotlib. , sphinx and sphinx-rtd-theme.

To use this project's code and personalize it, you should consider the libraries numpy and matplotlib for simulation, 
sphinx and sphinx-rtd-theme for documentation, and twine.


Install from pypi
***********************

You can install the library from `pypi <https://pypi.org/project/GenericSimulationLibrary/>`_. 
This is good for testing the library, but will **not** allow you to personalize the code.

.. code-block:: bash

    pip install GenericSimulationLibrary

Install from repository
***********************

You can install the library from github. This is good for testing the library, 
but will **not** allow you to personalize the code.

.. code-block:: bash

    pip install git+https://github.com/sebastiandres/GenericSimulationLibrary.git

Clone repository and install
******************************

You can clone the library from github. This is good for testing the library **and** 
will allow you to personalize the code.

.. code-block:: bash

    git clone https://github.com/sebastiandres/GenericSimulationLibrary.git
    cd GenericSimulationLibrary
    python setup.py install

Clone repository and install, but record installation files
************************************************************

Optionally, record the files installed, in case you want to remove them later:

.. code-block:: bash

    python setup.py install --record installation_files.txt

To uninstall removing the files:

.. code-block:: bash
    
    cat installation_files.txt | xargs sudo rm -rf
