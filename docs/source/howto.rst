How to use it
==============

*Ok, I'm in. What should I do?* 

Considerations
********************************
Through this explanation, let's asume you have the username `my-username`, that you will rename 
the project name from `GenericSimulationLibrary` to `MyProject` and that you will rename the class `SimulationInterface` 
to `MyInterface`.

Getting the code and versioning
********************************

You should start by getting a copy of the repo to play around: 
`<https://github.com/sebastiandres/GenericSimulationLibrary>`_.

There are several ways to do this. 

The first option: if you have a github account, you can fork the project to your github account.  
You can then clone **your** project to your local environment to start making changes:

.. code-block:: bash

    git clone https://github.com/PUT-YOUR-USERNAME-HERE/GenericSimulationLibrary.git

The second option is to download the `zip <https://github.com/sebastiandres/GenericSimulationLibrary/archive/master.zip>`_ 
file of the repository from the repository github's webpage. 
This allows to start with no previous commits. 
But now you need to add the project to your github account.

In both cases, you'll have full control to version the project and push your changes. 
You should end up with a project stored at `https://github.com/my-username/MyProject`

Test it by making a small change of the README.md, making a commit and pushing it. 
If you don't know how to do any of those, look at a tutorial like `<https://try.github.io/>`_. 

It may look as a overkill to do **git-versioning** and **library versioning** for your small project. **It is not**. 
Learn the tools and you will save an HUGE amount of time and frustration. Smash those bugs and document the code increments.

Personalize the Simulation Code
*********************************

The provided code already takes into account a **simple interface** and the creation of a **simulation seed**. 
Henceforth, code complexity is been hiden from the end user and a "simulation seed" can store 
all the information (inputs, system and libraries configuration, options and outputs) to guarantte reproducibility. 

To personalize the code, you need to replace the mentions to **GenericSimulationLibrary** and **SimulationInterface** 
with the choosen names, in this example, MyProject and MyInterface. 
You should edit the files at `GenericSimulationLibrary/GenericSimulationLibrary/` (in your project shoul be at `MyProject/GenericSimulationLibrary/`), in particular `simulation_interface.py` and `__init__.py`.
You can add more files if needed.

The code version is centralized and stored at `MyProject/GenericSimulationLibrary/version.py`. 
Follow some updating rule.

Personalize the Documentation
*******************************

The documentation is stored at `GenericSimulationLibrary/docs/source/` (in your project shoul be at `MyProject/docs/source`) 
You should personalize all the rst files. 
The files should give you some pointers on how to use, but you can consult the `rst specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_

To rebuilt the documentation, execute the following at the path `GenericSimulationLibrary/docs/` (or `MyProject/docs/` at your project):

.. code-block:: bash

    make clean
    make html

You can check how the documentation turn out at `GenericSimulationLibrary/docs/build/` (or `MyProject/docs/build` at your project), 
the main file being `index.html`.

You can now go to `read-the-docs <https://readthedocs.org/>`_ and import your library documentation to make it public.

Distribution
****************

The project is a **pip-installable library**. This has been taken care in the project structure and the file `setup.py`. 
You should edit `setup.py` and own it: make the changes of library name, version, author, packages, repository url, licence and description.

The project can be distributed from day one from the github repository. 

If you have a stable version, that you would like to distribute through pypi. 
There's a nice `pypi tutorial <https://packaging.python.org/tutorials/packaging-projects/>`_ you can follow. 

You need to have installed twine (`pip intall twine`), and to have accounts at `pypi <https://pypi.org/>`_ and `test.pypi <https://test.pypi.org/>`_. 
Note that that they required different accounts.

First, at the main folder, test the distribution at testpypi:

.. code-block:: bash

    python setup.py sdist bdist_wheel
    python -m twine upload --repository testpypi dist/*

There's a Makefile, so you can also just do `make test.pypi` at `GenericSimulationLibrary/` 
(in your project shoul be at `MyProject/`) 

You can check how everything looks at https://test.pypi.org/. 
If everything is looking good, upload it to (real) pypi:

.. code-block:: bash

    python setup.py sdist bdist_wheel
    python -m twine upload --repository pypi dist/*

Using the Makefile, you can just do `make pypi` at `GenericSimulationLibrary/` 
(in your project shoul be at `MyProject/`) 



