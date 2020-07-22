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

The objective is to provide a simple interface to solve reaction diffusion equations with 
a python library.
