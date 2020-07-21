from pypsdier import SimulationInterface

inputs = {
         "x_min":0, 
         "x_max":10, 
         "N_points":12,
         "m":3.0,
         "b":-2.0
}
plot_options = {
         "xlabel":"x [x_units]",
         "ylabel":"y [y_units]",
         "title":"My title",
         "data_x":[ 0.1, 2.1,  3.9,  6.1,  7.9,  9.9],  
         "data_y":[-2.8, 3.6, 10.7, 13.6, 22.8, 27.1],  # -2 + 3*x + error
         "data_kwargs": {'label':'exp', 'color':'red', 
                         'marker':'s', 'markersize':6, 
                         'linestyle':'none','linewidth':2, 
         },
         "sim_kwargs": {'label':'sim', 'color':'black', 
                         'marker':'o', 'markersize':6, 
                         'linestyle':'dashed','linewidth':2, 
         },
}
filepath = "test.sim"
print("Sim file:", filepath)

SI = SimulationInterface()
SI.new(inputs, plot_options)
SI.simulate()
SI.save(filepath)
SI.status()
del SI

SI_2 = SimulationInterface()
SI_2.load(filepath)
SI_2.plot(filename="test.png")
SI_2.status()
