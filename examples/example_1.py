# -*- coding: utf-8 -*-
import pypsdier
from math import exp

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

def CatalystEnzymeConcentration(t):
  """
  Enzyme Concentration in the catalyst particles, can vary in time due to several effects. 
  """
  E0 = 0.10 # [mM], initial concentration
  return E0*exp(-.1*t) # [mM]

################################################################################
# THE DICT inputs WILL CONTAIN ALL THE REQUIRED INFORMATION
# MUST PROVIDE A UNIQUE SEED FOR THE EXPERIMENT (WILL OVERWRITE FILE IF EXISTS)
# Names, InitialConditions, EffectiveDiffusionCoefficients MUST HAVE THE SAME NUMBER OF ELEMENTS
# Radiuses, RadiusesFrequencies MUST HAVE THE SAME NUMBER OF ELEMENTS
# ReactionParameters NEEDS TO BE COMPATIBLE WITH THE DEFINITION OF THE ReactionFunction
################################################################################
inputs = {}
inputs["SeedFile"] = "example_1.rde" # filename where the simulation will be stored
inputs["SimulationTime"] = 10. # [s], total time to be simulated 
inputs["SavingTimeStep"] = 1. # [s], saves only one data per second
inputs["CatalystVolume"]  = 0.01 # [mL], total volume of all catalyst particles in reactor
inputs["BulkVolume"]  = 40.0  # [mL], bulk volume of the liquid phase
inputs["Names"] = ('PenG',)  # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (1.3,)   # [mM], initial concentration of substrates and products
inputs["EffectiveDiffusionCoefficients"] = (5.30E-10,)  # [m2/s], effective diffusion coefficient for substrates and products
inputs["CatalystParticleRadius"] = [25.E-6, 50.E-6] # [m], list of possible catalyst particle radiuses
inputs["CatalystParticleRadiusFrequency"] = [0.5, 0.5] # [], list of corresponding frequencies of catalyst particle radiuses
inputs["ReactionFunction"] = MichaelisMenten # function defining the reaction 
inputs["ReactionParameters"] = (41 , 0.13)   # [1/s], [mM/s], parameters to be used in the reaction function after Cs and E0 
inputs["CatalystEnzymeConcentration"] = 0.001 #CatalystEnzymeConcentration # [mM] can be a float, int or a function returning float or int. 

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
SI.save("example_1.rde")
#SI.plot(filename="example_0.png")
SI.export_xls("example_1.xls")