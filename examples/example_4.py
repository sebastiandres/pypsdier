# -*- coding: utf-8 -*-
import pypsdier

################################################################################
# AUXILIAR DEFINITIONS OF REACTION AND ENZIMATIC CHARGE
################################################################################
def ReaccionCefalexina(Cs, E0, k1 ,k2, k3, k_3):
  """
  ReaccionCefalexina(Cs, E0, params)
  E0 [mM]
  params = k1 ,k2, k3, k_3 [mM]
  """
  ADCA, CEX, FG, FGME = Cs
  mcd = k1*FGME + k2 + k3*ADCA + k_3*CEX
  v_S = E0*k1*k3*FGME*ADCA / mcd
  v_H = E0*k2*k_3*CEX / mcd
  v_E = E0*k1*k2*FGME / mcd
  v = [ v_H - v_S, v_S - v_H, v_H + v_E, -v_S - v_E ]
  return v
E0 = 0.132
params = 56.5/60.,3407.4/60.,101.1/60.,14.3/60.  #[mM/s] 

################################################################################
# THE DICT params WILL CONTAIN ALL THE REQUIRED INFORMATION
# MUST PROVIDE A UNIQUE SEED FOR THE EXPERIMENT (WILL OVERWRITE FILE IF EXISTS)
# Names, InitialConditions, EffectiveDiffusionCoefficients MUST HAVE THE SAME NUMBER OF ELEMENTS
# Radiuses, RadiusesFrequencies MUST HAVE THE SAME NUMBER OF ELEMENTS
# ReactionParameters NEEDS TO BE COMPATIBLE WITH THE DEFINITION OF THE ReactionFunction
################################################################################
inputs = {}
inputs["SeedFile"] = "example_4.rde" # filename where the simulation will be stored
inputs["SimulationTime"] = 5. # [s], total time to be simulated 
inputs["SavingTimeStep"] = 1. # [s], saves only one data per second
inputs["CatalystVolume"]  = 0.146 # [mL], total volume of all catalyst particles in reactor
inputs["BulkVolume"]  = 25.0  # [mL], bulk volume of the liquid phase
inputs["Names"] = ('ADCA', 'CEX', 'FG', 'FGME') # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (0., 0., 0., 10.92) # [mM], initial concentration of substrates and products
inputs["EffectiveDiffusionCoefficients"] = (5.71E-10, 5.09E-10, 5.68E-10, 5.65E-10)  # [m2/s], effective diffusion coefficient for substrates and products
inputs["CatalystParticleRadius"] = (75.7E-6,) # [m], list of possible catalyst particle radiuses
inputs["CatalystParticleRadiusFrequency"] = (1.0,) # [], list of corresponding frequencies of catalyst particle radiuses
inputs["ReactionFunction"] = ReaccionCefalexina # function defining the reaction 
inputs["ReactionParameters"] = params   # [mM/s], parameters to be used in the reaction function 
inputs["CatalystEnzymeConcentration"] = E0 # [mM] can be a float, int or a function returning float or int. 

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
SI.save("example_4.rde")
#SI.plot(filename="example_0.png")
SI.export_xls("example_4.xls")