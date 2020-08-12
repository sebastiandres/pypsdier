Introduction
============

The immobilization of enzymes is a requisite for the re-use of these catalysts in repeated cycles in batch configuration or in continuous reactors. The recovery and/or retention of the enzyme catalyst is technical and economically feasible when micrometric or milimetric particles are used. The covalent attachment of the enzyme molecule to a porous solid support have shown high stabilization with different enzymes. Therefore, immobilization is neccessary and convinient for the efficient utilization of enzymes in technological processes. The reaction now occurs in a heterogeneous system composed by the solid catalysts particles and the bulk liquid. The catalysis is carried out inside the particle porous instead of the bulk liquid solvent. The inmediate consequence of this fact is that, along with the reaction, mass transfer is parallely occurring. The modeling of this heterogeneous process must considers reaction and diffusion components in the reactor performance equation. Theoretical and experimental approaches dealing with reaction-diffusion equations have been published in several articles.

Why do we care so much? 
*************************

In 2008, we started the development of numerical implementation of 
generic reaction diffusion equations for reactors using catalysts prepared by enzyme immobilization on small porous particles.
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
