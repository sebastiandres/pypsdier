import numpy as np
from matplotlib import pyplot
import pypsdier.core.seed_library as seed
from pdb import set_trace as st

# Experimentals results from a batch experiment
t_exp = np.array([ 0,  2,  4,  6,  8,
                  10, 20, 30, 40, 50,
                  65, 80,100,120,150]) # Time in mins
PenG_exp = np.array([10.00, 9.68, 9.3 , 8.93, 8.85,
                      8.7 , 8   , 6.5 , 5.21, 3.59, 
                      2.58, 1.65, 1.01, 0.49, 0.25])
# Numerical results
seedfile = "PGA650R72.rde"
params = seed.grow(seedfile)

# Unpack the ODE and PDE results
t_sim_ode = params["ODE"]["t"] / 60. # in minutes
PenG_sim_ode = params["ODE"]["C"][:,0]
t_sim_pde = params["PDE"]["t"] / 60. # in minutes
PenG_sim_pde = params["PDE"]["C"][0][0][:,-1]

# Plot the different concentrations
fig = pyplot.figure()
ax = pyplot.subplot(111)
pyplot.plot(t_sim_ode, PenG_sim_ode, '--b', lw=2.0, alpha=0.5, label="Free enzyme")
pyplot.plot(t_sim_pde, PenG_sim_pde,   'b', lw=2.0, alpha=1.0, label="Immobilized enzyme")
pyplot.plot(t_exp, PenG_exp, 'ws', mew=2.0, label="Experimental data")
pyplot.xlabel("Time [min]")
pyplot.ylabel("PenG concentration [mM]")
#pyplot.title("Experimental results versus reaction / reaction diffusion models")
xlim = ax.get_xlim()
dx = .025*(xlim[1]-xlim[0])
ax.set_xlim(xlim[0]-dx, xlim[1]+dx)
ylim = ax.get_ylim()
dy = .025*(ylim[1]-ylim[0])
ax.set_ylim(ylim[0]-dy, ylim[1]+dy)
# Shink size to fit legend
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), 
          fancybox=True, shadow=True, ncol=3,
          numpoints=1) # Show only * instead of ** as marker legend
# Save figure
pyplot.savefig(seedfile.replace(".rde",".png"))
pyplot.show()
