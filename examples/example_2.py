# -*- coding: utf-8 -*-
import pypsdier

################################################################################
# AUXILIAR DEFINITIONS OF REACTION AND ENZIMATIC CHARGE
################################################################################
def ReaccionPenG(Cs, E0, k, K, Ks, K1, K2):
  """
  ReaccionPenG(Cs, E0, params)
  Cs = PenG [mM], AFA [mM], 6-APA [mM]
  E0 [mM]
  params = k [1/s], K [mM], Ks [mM], K1 [mM], K2 [mM]
  """
  PenG, AFA, APA6 = Cs
  mcd = K+PenG+PenG*PenG/Ks+K*AFA/K1+K*APA6/K2+PenG*APA6/K2+K*AFA*APA6/(K1*K2)
  v_S = k*E0*PenG/mcd
  v = (-v_S, v_S, v_S )
  return v

################################################################################
# THE DICT params WILL CONTAIN ALL THE REQUIRED INFORMATION
# MUST PROVIDE A UNIQUE SEED FOR THE EXPERIMENT (WILL OVERWRITE FILE IF EXISTS)
# Names, InitialConditions, EffectiveDiffusionCoefficients MUST HAVE THE SAME NUMBER OF ELEMENTS
# Radiuses, RadiusesFrequencies MUST HAVE THE SAME NUMBER OF ELEMENTS
# ReactionParameters NEEDS TO BE COMPATIBLE WITH THE DEFINITION OF THE ReactionFunction
################################################################################
inputs = {}
inputs["SeedFile"] = "example_2.rde" # filename where the simulation will be stored
inputs["SimulationTime"] = 1.*60 # [s], total time to be simulated 
inputs["SavingTimeStep"] = 1. # [s], saves only one data per second
inputs["CatalystVolume"]  = 0.100 # [mL], total volume of all catalyst particles in reactor
inputs["BulkVolume"]  = 40.0  # [mL], bulk volume of the liquid phase
inputs["Names"] = ('PenG', 'AFA', '6-APA')  # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (10.0, 0., 0.)   # [mM], initial concentration of substrates and products
inputs["EffectiveDiffusionCoefficients"] = (5.30E-10, 7.33E-10, 5.89E-10)  # [m2/s], effective diffusion coefficient for substrates and products
inputs["CatalystParticleRadius"] = (100.E-6,) # [m], list of possible catalyst particle radiuses
inputs["CatalystParticleRadiusFrequency"] = (1.0,) # [], list of corresponding frequencies of catalyst particle radiuses
inputs["ReactionFunction"] = ReaccionPenG # function defining the reaction 
inputs["ReactionParameters"] = 41., 0.13, 821., 1.82, 48.  #[1/s] and [mM]*4  # [1/s], [mM/s], parameters to be used in the reaction function 
inputs["CatalystEnzymeConcentration"] = 0.164 # [mM] can be a float, int or a function returning float or int. 


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
SI.save("example_2.rde")
#SI.plot(filename="example_0.png")
SI.export_xls("example_2.xls")