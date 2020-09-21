Equations
===================================================

Variables and parameters
--------------------------

Let's consider a substance :math:`S`. Let's call: 

* :math:`S_b(t)`: Concentration of the substance on the bulk (liquid) phase, outside all particles. 
  The substance could be a substract or a product of the reaction. It is usually measured in mols per liter.
* :math:`V_b`: Total volume of the bulk (liquid) phase. Usually measured in liters.
* :math:`S(t,r,R_i)`: Concentration at time :math:`t` and radial position :math:`r`, 
  inside a particle of radius :math:`R_i`. Measured in the same units of :math:`S_b(t)`.
* :math:`f(R)`: Particle size distribution. Typically, this is a discrete approximation of the real
  (measurable but ultimately unknown) particle size distribution. For practical purposes 
  we will consider a finite discrete distribution with :math:`N_R` different particle sizes, where the 
  probability :math:`p_i` for a particle having radius :math:`R_i` for 
  :math:`i \in \{1, 2, \cdots, N_R \}` with :math:`\sum_{i=1}^{N_R} p_i = 1`.
* :math:`V_R`: total volume of particles, experimentally obtained with the total weight and density of the catalyst particles.
  Measured in the same units as :math:`V_b`.
* :math:`D_S`: Effective diffusion coefficient of substance :math:`S` inside the (porous) particle. It has the units 
  meters squared / second. 
* :math:`v_e`: Effective reaction rate at which the amount of substance :math:`S` changes
  without considering diffusional restrictions. If :math:`v_e>0` it is ussually called a product, while :math:`v_e<0` is called a substract. 
  This is usually measured in the units of :math:`S_b` per second. 

Impact of a particle distribution
---------------------------------------

We define :math:`N_R` the number of different particle radii. 
A discrete particle size distribution has probability :math:`p_i` 
for a particle having radius :math:`R_i`, for :math:`i \in \{1, 2, \cdots, N_R \}` 
with :math:`\sum_{i=1}^{N_R} p_i = 1`.  The probability :math:`p_i` is interpreted 
in a frequentist approach: it is simply the fraction of particles of the size :math:`R_i`, given by 
:math:`p_i = n_i / n` with :math:`n = \sum_{i=1}^{N_R} n_i` being the total number of particles.

We can then work out explicitely the total number of particles from the total volume of the particles:  

.. math::
   V_R & = \sum_{i=1}^{N_R} n_i \frac{4 \pi}{3} R_i^3 = \sum_{i=1}^{N_R} p_i \ n \  \frac{4 \pi}{3} R_i^3 \\ 
      & = n \  \frac{4 \pi}{3} \sum_{i=1}^{N_R} p_i R_i^3

That is, the total number of particles is given 
by the total volume and the expected volume of a single particle.

.. math::
   n_i = p_i n = p_i \frac{V_R}{\frac{4 \pi}{3} E \left[ R^3 \right]}

Let's consider a numerical example. Let's imagine we have only two particle sizes: 
:math:`R_1 = 0.9 R_0` and :math:`R_2 = 1.1 R_0` with a given parameter :math:`R_0`.
One has a particle volume 
:math:`V_1 = \frac{4 \pi}{3} R_1^3 = 0.9^3 \frac{4 \pi}{3} R_0^3 \approx 0.729 V_0`.
The other has particle volume 
:math:`V_21 = \frac{4 \pi}{3} R_2^3 = 1.1^3 \frac{4 \pi}{3} R_0^3 \approx 1.332 V_0`.
If the distribution is uniform, :math:`p_1=p_2=0.5`, 
that means that there are as many particles of size :math:`R_1` as :math:`R_2`, 
:math:`n_1 = 0.5 n = n_2`. 

Nevertheless, in terms of total volume we have

.. math::
   V_R &= n_1 V_1 + n_2 V_2 \\
       &= p_1 n V_1 + p_2 n V_2 \\
       &= 0.5 \times 0.729 \ n + 0.5 \times 1.332 \ n \\

That means that the total volume of particles of size R_1 makes up for 35% of the total volume,
while the R_2 makes up for the other 65%. 
Notices that a symmetric 10% difference from a reference value creates a 15% difference 
from a uniform volume distribution.

How to model the effective reaction rate 
---------------------------------------------

The effective reaction rate :math:`v_e` is a function of several terms, 
and applies only inside the particles (where the catalist exists). 
In a particle of radius :math:`R_i`, it would be:

.. math::
   v_e(t,r,R_i) 
   &= v_e \left( S(t,r,R_i), E(t,r, R_i), \textrm{other relevant parameters} \right) \\
   & \approx v \left( S(t,r,R_i), E_{max}, \textrm{other relevant parameters} \right) \times I(t) \times Z(r, R_i) 

Where: 

* :math:`v(S, E, \textrm{other relevant parameters})`: the reaction rate, measured in  the units of :math:`S_b` per second.
* :math:`I(t)`: Enzime Inactivation. It only possess time dependance, being bounded between 0 and 1: :math:`0 \leq I(t) \leq 1`. It has no units.
* :math:`Z(r, R_i)`: Enzime radial distribution (again, no units), :math:`0 < Z(r, R_i)` and such that the total enzime applied to all particles is a known value :math:`E_0`:

.. math::
   E_0 &= \sum_{i=1}^{N_R} n_i \int_0^{R_i} E_{max} Z(r, R_i) 4 \pi r^2 dr \\
   &= n \sum_{i=1}^{N_R} \frac{n_i}{n} \int_0^{R_i} E_{max} Z(r, R_i) 4 \pi r^2 dr \\ 
   &= \frac{V_R}{\sum_{i=1}^{N_R} p_i 4/3 \pi R_i^3 } \sum_{i=1}^{N_R} p_i \int_0^{R_i} E_{max} Z(r, R_i) 4 \pi r^2 dr \\
   &= 3 \frac{V_R E_{max} }{\sum_{i=1}^{N_R} p_i R_i^3 } \sum_{i=1}^{N_R} p_i \int_0^{R_i} Z(r, R_i) r^2 dr

Here we have used :math:`n_i` the number of particles of size :math:`R_i`, :math:`n` the total number of particles,
and the relationship between volume and particle size distibution:

.. math::
   V_R = \sum_{i=1}^{N_R} n_i \frac{4}{3} \pi R_i^3 = n \sum_{i=1}^{N_R} \frac{n_i}{n} \frac{4}{3} \pi R_i^3
       = n \sum_{i=1}^{N_R} p_i \frac{4}{3} \pi R_i^3 = \frac{4 \pi n}{3} E \left[ R^3 \right]


The equations
---------------

The equations, boundary conditions and initial conditions are given for :math:`S_b(t)` and :math:`S(t,r,R_i)`.

The reaction diffusion equation, for :math:`t>0` and :math:`0<r<R_i`: 

.. math:: 
   \frac{\partial S}{\partial t}(t,r,R_i) = D_S \left(\frac{\partial^2 S}{\partial r^2}(t,r,R_i) 
   + \frac{2}{r}\frac{\partial S}{\partial r}(t,r,R_i)\right) - V\left(S(t,r,R_i)\right) I(t) Z(r, R_i)

The boundary condition at the center of the particle comes out from by imposing 
that there can not be any flux through the center of the sphere. This is, for :math:`t>0`:

.. math:: 
   \frac{\partial S}{\partial r}(t, 0, R_i) = 0

The boundary conditions at the surface of the particles are 

.. math:: 
   S_b(t)  = S(t, R_i,R_i)

and 

.. math:: 
   \frac{d S}{d t}(t, R_i, R_i)  
   &= - 3 D_S \frac{V_c}{V_R E \left[ R^3 \right] } E \left[ R^2 \left. \frac{\partial S}{\partial r} \right|_{r=R} \right] \\
   &= - 3 D_S \frac{V_c}{V_R \sum_{i=1} ^{N_R} R_i^3} \sum_{i=1} ^{N_R} R_i^2  \frac{\partial S(t,R_i, R_i)}{\partial R} \\

Which come from the continuity on the surface for the variables and the flux condition.

The initial conditions are 

.. math:: 
   S_b(0) &= S_0 \\
   S(0,r, R_i) &= 0 \textrm{ for } 0 \leq r < R_i