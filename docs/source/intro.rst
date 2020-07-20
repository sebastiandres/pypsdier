Introduction
============

Why do we care so much? 
*************************

In 2008, we started the development of numerical implementation of 
generic reaction diffusion equations 
of catalysts immobilized on small porous particles. 
Python was a great choice back then, as it provided a language that was simple and high level, 
but still fast enough. Nevertheless, the python installation, versioning and library 
updates were messy and required constant supervision and side by side work. 
We longed for a simpler method. 
Fast travel to 2020, where you can now run python code on your browser on a server. 
You can now really collaborate with anyone on the planet and make sure the simulation 
is being run exactly as supposed. We've been reflecting on the key elements that are 
required on a simulation framework that provides this kind of "SaaS behavior". 
How could you make things as easy as possible for the other party while, as a developer, 
still been able to have full control on the code and guarantee the reproducibility of results?

Objective
***********

The objective is to provide a working answer for the following constrains:

* Dealing with installation and versioning of python, jupyter and libraries.

* Simplifying the deployment and versioning of a specific piece of code (the custom simulation library).

* Exposing a simple interface to the final user to hied a (complex) numerical implementation.

* Allowing to store and share simulation results, so that they can be reproduced and analyzed.

* Allowing to use external computational resources, so that the simulation doesn't take a toll on your cheap notebook.

Solution
*********

We think the objetive can be obtained with a code with the following characteristics:

* **pip-installable library**: this allows for a flexible approach. You can install nothing at all and run everything on google colab, or install it locally. But it's your call, and you are not forced to run everything on local (thanks free cloud providers!). This addresses for installation and versioning.

* **git-versioning** and **library versioning**: smash those bugs and document the code increments. This addresses reproducibility and versioning.

* **simple interface**: hide the complexity of the code with some OO to make it simple for the end user.

* **simulation seed**: the library should create a "simulation seed" that contains all the information (inputs, system and libraries configuration, options and outputs). This "simulation seed" can be stored and shared on itself, or together with a jupyter notebooks. This addresses the reproducibility.

Limitations
***********

* Does not contains any Monthy Python jokes. If you have a good one, please send it!

* It's just a framework with simplistic inputs and simulation code. You **will** need to personalize the class SimulationInterface and all its methods.