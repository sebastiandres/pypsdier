import pypsdier
import os
"""
Description: This is the simulation and experimental data for the 
Hydrolysis Reaction of Penicilin G.
"""

def PenG_HydrolysisReaction(Cs, E0, k, K, Ks, K1, K2):
  """
  ReaccionPenG(Cs, E0, inputs)
  Cs = PenG [mM], AFA [mM], 6-APA [mM]
  E0 [mM]
  inputs = k [1/s], K [mM], Ks [mM], K1 [mM], K2 [mM]
  """
  PenG, AFA, APA6 = Cs
  mcd = K + PenG + PenG*PenG/Ks + K*AFA/K1 + K*APA6/K2 + PenG*APA6/K2 + K*AFA*APA6/(K1*K2)
  v_S = (k*E0*PenG) / mcd
  v = (-v_S, v_S, v_S )
  return v

inputs = {}
inputs["SeedFile"] = "PGA400R72.rde" # filename where the simulation will be stored
inputs["SimulationTime"] = 120.*60 # [s], total time to be simulated 
inputs["SavingTimeStep"] = 60. # [s], saves only one data per second
inputs["CatalystVolume"] = 0.0350 # [mL], total volume of all catalyst particles in reactor
inputs["BulkVolume"] = 40.3  # [mL], bulk volume of the liquid phase
inputs["Names"] = ('PenG', 'AFA', '6-APA')  # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (10.0, 0., 0.)   # [mM], initial concentration of substrates and products
inputs["EffectiveDiffusionCoefficients"] = (5.30E-10, 7.33E-10, 5.89E-10)  # [m2/s], effective diffusion coefficient for substrates and products
inputs["CatalystParticleRadius"] = (75.7E-6,) # [m], list of possible catalyst particle radiuses
inputs["CatalystParticleRadiusFrequency"] = (1.0,) # [], list of corresponding frequencies of catalyst particle radiuses
inputs["ReactionFunction"] = PenG_HydrolysisReaction # function defining the reaction 
inputs["ReactionParameters"] = 41., 0.13, 821., 1.82, 48.  #[1/s] and [mM]  parameters to be used in the reaction function 
inputs["CatalystEnzymeConcentration"] = 0.106 # [mM] can be a float, int or a function returning float or int.

plot_options = {}
plot_options["t_exp"] = [0, 2, 4, 6, 8, 10, 20, 30, 45, 60, 80, 100, 120] # Time in mins
plot_options["PenG_exp"] = [10.00, 9.46, 9.01, 8.56, 8.17, 7.79, 5.63, 3.90, 2.06, 0.95, 0.35, 0.12, 0] # Concentration

# Define filename for storing the simulation and plots
filename = "PGA400R72.rde"

# Simulate only if file not found
SI = pypsdier.SimulationInterface()
if os.path.exists(filename):
    SI.load(filename)
else:
    SI.new(inputs, plot_options)
    SI.simulate("ode")
    SI.simulate("pde")
    SI.save(filename)
SI.status()
SI.plot("plot", display=True)
SI.export_xls(filename.replace(".rde", ".xls"))