# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import numpy as np
import sys

################################################################################
# MAIN SOLVER OF THE ODE
################################################################################
def ode_solver(ode_params, master_file=sys.argv[0]):
  """
  Wrapper for using scipy ode solver with our notation 
  """
  print("Solving the equivalent ode equation.")
  # Unpacking the values
  Reaction = ode_params["ReactionFunction"]
  params = ode_params["ReactionParameters"]
  Tsim = ode_params["SimulationTime"]
  Vc = ode_params["CatalystVolume"]
  Vb = ode_params["BulkVolume"]
  legend = ode_params["Names"]
  IC = ode_params["InitialConcentrations"]
  D = ode_params["EffectiveDiffusionCoefficients"]
  E0 = ode_params["CatalystEnzymeConcentration"]
    
  # DEFINING A LOCAL REACTION
  # E0 must be corrected for incluying dilution
  dilusion = Vc / Vb # Catalyst is in 10% dilution ratio

  def diluted_E(t, dilution):
    if type(E0)==float or type(E0)==int:
      return dilusion*E0
    else:
      return dilusion*E0(t)

  def ode_reaction(C, ti, E0, dilusion, local_params):
    E_t = diluted_E(ti, dilusion)
    return Reaction(C, E_t, *params)

  # DEFINING THE TIME TO SIMULATE
  dt = 0.01
  if "PDE" in ode_params:
    T = ode_params["PDE"]["t"]
  else:
    T = np.arange(0.0, Tsim+dt, dt) 

  # ODE SOLUTION 
  C = odeint(ode_reaction, IC, T, args=(diluted_E, dilusion, params))

  # Adding the new information to the dict
  ode_solution_dict = {"t":T, 
                       "C":C, 
                       "dt":dt,
                       "diluted_E":np.array([diluted_E(ti, dilusion) for ti in T]), 
                       "method":"scipy.odeint"}
  return ode_solution_dict
