Examples
=============

Example in Google colab
************************
Here is an executable example using `Google Colab <https://htmlpreview.github.io/?https://github.com/sebastiandres/pypsdier/blob/master/demo/colab_test.html>`_. 
Requires a google account (but it's worth it :).

Example in mybinder
*********************

Here is an executable example using `MyBinder <https://htmlpreview.github.io/?https://github.com/sebastiandres/pypsdier/blob/master/demo/binder_test.html>`_.
Does not requires any account, but it will not store results.

Code example
*********************
To run all the next lines you need to install the library. 
We hope you'll appreciate that all you need is to define the inputs and plot options, and run the simulation. 
Libraries and outputs are silently handled. 
Saving, plotting or exporting the results is trivially easy for the user.

We'll define the simplest experiment possible.

The first thing is to setup the inputs and plotting options.
This requires to define dictionaries with specific keys.

.. code-block:: python
    
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


Creating a new simulation requires to use a new simulation interface. 

.. code-block:: python

    import pypsdier
    SIM = pypsdier.SimulationInterface()
    SIM.new(inputs, plot_options)


To simulate you need to the corresponding method:

.. code-block:: python
    
    SIM.simulate("pde")
    SIM.simulate("ode")


At any point of the code you can use the `status` method to know if the required libraries are installed, what are the inputs, plot options and simulation statuses.

.. code-block:: python
    
    SIM.status()


You can plot the results with the `plot` method. If needed, you can update the plot_options dictionary.
Use `plot?` to know available plotting arguments.

.. code-block:: python
    
    SIM.plot()


You can generate and download a compressed simulation file, so you can late load your results

.. code-block:: python
    
    SIM.save("SIM.rde")


Or you can generate an excel file to explore the results to use a more familiar program.

.. code-block:: python

    SIM.export_xls("SIM.xls")
