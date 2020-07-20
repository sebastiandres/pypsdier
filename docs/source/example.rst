Examples
=============

Example in Google colab
************************
Here is an executable example using `Google Colab <https://colab.research.google.com/drive/1mfSZQOhe7qq1C-YpfX5dDpSedXGVjz4e?usp=sharing>`_. 
Requires a google account (but it's worth it :).

Example in mybinder
*********************

Here is an executable example using `MyBinder <https://mybinder.org/v2/gh/sebastiandres/GenericSimulationLibrary/master?filepath=tests%2Fjupyter_test.ipynb>`_.
Does not requires any account, but it will not store results.

Code example
*********************
To run it, you need to install the library. 

To run and save a simulation:

.. code-block:: python

    from GenericSimulationLibrary import SimulationInterface

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
    filepath = "/test.sim"
    print("Sim file:", filepath)

    SI = SimulationInterface()
    SI.new(inputs, plot_options)
    SI.simulate()
    SI.save(filepath)
    SI.status()
    del SI
    
To load a simulation and plot the results:

.. code-block:: python

    from GenericSimulationLibrary import SimulationInterface
    SI_2 = SimulationInterface()
    SI_2.load(filepath)
    SI_2.plot(filename="test.png")
    SI_2.status()

As you can see, all you need is to define the inputs and plot options, and run the simulation. 
Libraries and outputs are silently handled. 
Saving, plotting or exporting the results is trivially easy for the user.
