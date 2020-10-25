def MichaelisMenten(S, E0, k, K):
  """Definition for Michaelis Menten reaction with inputs E0 [mM], k [1/s] and K [mM]"""
  return (-k*E0*S[0]/(K+S[0]), )

inputs = {}
inputs["SimulationTime"] = 120. # [s]
inputs["SavingTimeStep"] = 1. # [s]
inputs["CatalystVolume"] = 0.5 # [mL]
inputs["BulkVolume"]  = 100.0  # [mL]
inputs["Names"] = ('Substrat',)  # legend for the xls, reports and plots
inputs["InitialConcentrations"] = (1.3,)   # [mM]
inputs["EffectiveDiffusionCoefficients"] = (5.3E-10,)  # [m2/s]
inputs["CatalystParticleRadius"] = [40.0E-6, 60.0E-6, 80.0E-6] # [m]
inputs["CatalystParticleRadiusFrequency"] = [0.3, 0.5, 0.2] # []
inputs["ReactionFunction"] = MichaelisMenten # function 
inputs["ReactionParameters"] = (41 , 0.13)   # [1/s], [mM/s], parameters
inputs["CatalystEnzymeConcentration"] = 0.35 # [mM]

plot_options = {}
plot_options["title"] = "Simulación de Michaelis Menten para la PyconAr"
plot_options["label_x"] = "Tiempo de reacción [s]"
plot_options["label_y"] = "Concentración [mM]"
plot_options["ode_kwargs"] = {'label':'ode', 'color':'black', 'marker':'', 'markersize':6, 'linestyle':'dashed', 'linewidth':2}
plot_options["pde_kwargs"] = {'label':'pde', 'color':'black', 'marker':'', 'markersize':6, 'linestyle':'solid', 'linewidth':2}
plot_options["data_kwargs"] = {'label':'exp', 'color':'red', 'marker':'s', 'markersize':6, 'linestyle':'none', 'linewidth':2}
plot_options["data_x"] = [0.0, 30, 60, 90, 120]
plot_options["data_y"] = [1.3, 0.65, 0.25, 0.10, 0.0]

# import pypsdier
import pypsdier
SIM1 = pypsdier.SimulationInterface()
SIM1.new(inputs, plot_options)
SIM1.status()

SIM1.simulate("pde")

SIM1.simulate("ode")

SIM1.save("pycon_ANOTHER_example.rde")

SIM1.export_xls("pycon_example.xls")

SIM1.plot()

#----
import pypsdier
SIM2 = pypsdier.SimulationInterface()
SIM2.load("pycon_saving_example.rde") # load instead of new
SIM2.status()

SIM2.export_xls("saving_to_another_excel_file.xls")

SIM2.plot()