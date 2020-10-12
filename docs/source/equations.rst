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

Let's consider a numerical example. Let's imagine we have a total volume of :math:`V_R = 10 \ [m l] = 1.0\ E-8 \ [m^3]`
Let's consider the following distribution :math:`p_1 = 0.4` and :math:`p_2 = 0.6`, 
for :math:`R_1 = 0.9 R_0` and :math:`R_2 = 1.1 R_0`, where :math:`R_0=6.5 \ E-9 \ [m]` respectively.

We can compute the following values:

* The expected radius is :math:`E[R] = p_1 R_1 + p_2 R_2 = XxX`
* The volume for a expected radius is :math:`\frac{4}{3} \pi (E[R])^3 = XxX`
* The number of particles is :math:`V_R / \frac{4}{3} \pi (E[R])^3 = XxX`.
* The number of particles of size :math:`R_1` and :math:`R_1` are :math:`n_1 = p_1 n = XxX` y :math:`n_1 = p_1 n = XxX`, respectively. 
* The total surface is 

How to model the effective reaction rate 
---------------------------------------------

The effective reaction rate :math:`v_e` is a function of several terms, 
and occurs only inside the particles, where the catalist is attached to the surface of the porous structure. 
In a particle of radius :math:`R_i`, it would be:

.. math::
   v_e(t,r,R_i) 
   &= v_e \left( S(t,r,R_i), E(t,r, R_i), \textrm{other relevant parameters} \right) \\
   & \approx v \left( S(t,r,R_i), E_{max}, \textrm{other relevant parameters} \right) \times I(t) \times Z(r, R_i) 

Where: 

* :math:`v(S, E, \textrm{other relevant parameters})`: the reaction rate, measured in  the units of :math:`S_b` per second.
* :math:`I(t)`: Enzime Inactivation. It only has time dependance, being bounded between 0 and 1 and decreasing: :math:`0 \leq I(t) \leq 1`. It has no units. It models tha catalyst inhibition growing over time.
* :math:`Z(r, R_i)`: Enzime radial distribution, that only has space dependance and being non-negative, :math:`0 < Z(r, R_i)`    and such that the total enzime applied to all particles is a known value :math:`E_0`:

.. math::
   E_0 &= \sum_{i=1}^{N_R} n_i \int_0^{R_i} E_{max} Z(r, R_i) 4 \pi r^2 dr \\
   &= n \sum_{i=1}^{N_R} \frac{n_i}{n} \int_0^{R_i} E_{max} Z(r, R_i) 4 \pi r^2 dr \\ 
   &= n E_{max} 4 \pi \sum_{i=1}^{N_R} p_i \int_0^{R_i} Z(r, R_i) r^2 dr

Here we have used :math:`n_i` the number of particles of size :math:`R_i`, 
and :math:`n` the total number of particles,
and the relationship between volume and particle size distibution:

.. math::
   n = \frac{V_R}{\frac{4 \pi}{3} E \left[ R^3 \right]}
     = \frac{V_R}{\sum_{i=1}^{N_R} p_i \frac{4}{3} \pi R_i^3} 

The equations
---------------

The equations, boundary conditions and initial conditions are given for :math:`S_b(t)` and :math:`S(t,r,R_i)`.

The reaction diffusion equation, for :math:`t>0` and :math:`0<r<R_i`: 

.. math:: 
   \frac{\partial S}{\partial t}(t,r,R_i) = D_S \left(\frac{\partial^2 S}{\partial r^2}(t,r,R_i) 
   + \frac{2}{r}\frac{\partial S}{\partial r}(t,r,R_i)\right) - v_e\left(S(t,r,R_i)\right) I(t) Z(r, R_i)

The boundary condition at the center of the particle for :math:`t>0`:

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

The initial conditions are 

.. math:: 
   S_b(0) &= S_0 \\
   S(0,r, R_i) &= 0 \textrm{ for } 0 \leq r < R_i \textrm{ and } i \in \{ 1, 2, \cdots, N_R \} 