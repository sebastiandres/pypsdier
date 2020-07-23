# -*- coding: utf-8 -*-
import pypsdier
from math import exp

"""
Description: This is a extremely basic example. We will have a unique fictional 
substract being consumed with a reaction modelled by Michaelis Menten equation. 
Values for the parameters have been handpicked for a quick simulation,
only for numerical reasons.
It has constant catalyst enzyme Concentration, and the enzymes are kept in
a unique catalyst of particle radii 100 [um].
"""
################################################################################
# AUXILIAR DEFINITIONS OF REACTION AND ENZIMATIC CHARGE
################################################################################
def MichaelisMenten(Cs, E0, k, K):
  """
  Definition for Michaelis Menten reaction with inputs k [1/s] and K [mM]
  """
  S, = Cs
  v_S = k*E0*S/(K+S)
  v = (-v_S,)
  return v

################################################################################
# THE DICT inputs WILL CONTAIN ALL THE REQUIRED INFORMATION
# MUST PROVIDE A UNIQUE SEED FOR THE EXPERIMENT (WILL OVERWRITE FILE IF EXISTS)
# Names, InitialConditions, EffectiveDiffusionCoefficients MUST HAVE THE SAME NUMBER OF ELEMENTS
# Radiuses, RadiusesFrequencies MUST HAVE THE SAME NUMBER OF ELEMENTS
# ReactionParameters NEEDS TO BE COMPATIBLE WITH THE DEFINITION OF THE ReactionFunction
################################################################################
inputs = {}
inputs["SimulationTime"] = 1*60. # [s], total time to be simulated 
inputs["SavingTimeStep"] = 10. # [s], saves only one data per second
inputs["CatalystVolume"]  = 0.01 # [mL], total volume of all catalyst particles in reactor
inputs["BulkVolume"]  = 40.0  # [mL], bulk volume of the liquid phase
inputs["Names"] = ('Substrat',)  # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (1.0,)   # [mM], initial concentration of substrates and products
inputs["EffectiveDiffusionCoefficients"] = (1.0E-9,)  # [m2/s], effective diffusion coefficient for substrates and products
inputs["CatalystParticleRadius"] = [100.E-6] # [m], list of possible catalyst particle radiuses
inputs["CatalystParticleRadiusFrequency"] = [1.0] # [], list of corresponding frequencies of catalyst particle radiuses
inputs["ReactionFunction"] = MichaelisMenten # function defining the reaction 
inputs["ReactionParameters"] = (41 , 0.13)   # [1/s], [mM/s], parameters to be used in the reaction function after Cs and E0 
inputs["CatalystEnzymeConcentration"] = 0.5 # [mM] can be a float, int or a function returning float or int. 

plot_options = {}
plot_options["xlabel"] = "x [x_units]"
plot_options["ylabel"] = "y [y_units]",
plot_options["title" ] = "My title",
plot_options["data_x"] = [ 0.1, 2.1,  3.9,  6.1,  7.9,  9.9],  
plot_options["data_y"] = [-2.8, 3.6, 10.7, 13.6, 22.8, 27.1],  # -2 + 3*x + error
plot_options["data_kwargs"] = {'label':'exp', 'color':'red', 
                         'marker':'s', 'markersize':6, 
                         'linestyle':'none','linewidth':2, 
         },
plot_options["sim_kwargs"] = {'label':'sim', 'color':'black', 
                         'marker':'o', 'markersize':6, 
                         'linestyle':'dashed','linewidth':2, 
         },

################################################################################
# SOLVE THE PDE AND SAVE THE RESULT INTO THE SEED
################################################################################
SI = pypsdier.SimulationInterface()
SI.new(inputs, plot_options)
SI.status()
SI.simulate("ode")
SI.simulate("pde")
SI.save("test_MM.rde")
del SI

SI2 = pypsdier.SimulationInterface()
SI2.load("test_MM.rde")
SI2.export_xls("example_0.xls")
SI2.simulate("ode")
SI2.simulate("pde")
SI2.save("test_MM2.rde")
SI2.status()
SI2.plot(filename="test_MM.png")
