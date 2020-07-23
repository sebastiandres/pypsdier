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
params = {}
params["SeedFile"] = "PGA650R72.rde" # filename where the simulation will be stored
params["SimulationTime"] = 150.*60 # [s], total time to be simulated 
params["SavingTimeStep"] = 60. # [s], saves only one data per second
params["CatalystVolume"] = 0.0215 # [mL], total volume of all catalyst particles in reactor
params["BulkVolume"] = 40.3  # [mL], bulk volume of the liquid phase
params["Names"] = ('PenG', 'AFA', '6-APA')  # legend for the xls, reports and plots
params["InitialConcentrations"] = (10.0, 0., 0.)   # [mM], initial concentration of substrates and products
params["EffectiveDiffusionCoefficients"] = (5.30E-10, 7.33E-10, 5.89E-10)  # [m2/s], effective diffusion coefficient for substrates and products
params["CatalystParticleRadius"] = (75.7E-6,) # [m], list of possible catalyst particle radiuses
params["CatalystParticleRadiusFrequency"] = (1.0,) # [], list of corresponding frequencies of catalyst particle radiuses
params["ReactionFunction"] = ReaccionPenG # function defining the reaction 
params["ReactionParameters"] = 41., 0.13, 821., 1.82, 48.  #[1/s] and [mM]*4  # [1/s], [mM/s], parameters to be used in the reaction function 
params["CatalystEnzymeConcentration"] = 0.140 # [mM] can be a float, int or a function returning float or int.

################################################################################
# SOLVE THE PDE AND SAVE THE RESULT INTO THE SEED
################################################################################
pypsdier.pde(params)
pypsdier.ode(params)
