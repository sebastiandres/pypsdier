import pickle
import sys

class SimulationInterface():
    """GenericSimulationLibrary is a package encapsulates a methodology 
    and tools for reproducible simulations. 
    The main idea is to use python and/or jupyter notebooks to provide a 
    lightweight and for-dummies easy “Simulation as a Service”. 
    The framework puts emphasis on simplicity: 
    for the client to install and use, 
    for the programmer to distribute and update, 
    and for everyone to store and reproduce results. 
    The framework can be personalized and extended for a specific simulation need.
    Link: https://pypsdier.readthedocs.io/
    """

    def __init__(self):
        """Initializes the class, with no inputs. 
        Will assume that if you have the colab library installed, 
        you're running on google colab(oratory). 

        :return: Nothing
        :rtype: Nothing
        """
        self.configuration = self.__get_configuration()
        self.inputs = {}
        self.plot_options = {}
        self.outputs = {}
        return

    def __get_configuration(self):
        """Carefully tries to import required libraries,
        storing the python and library version.

        :return: Nothing
        :rtype: Nothing
        """
        # Gets the library version
        from .version_file import version_number as GSL_version
        # Gets the python environmnet
        try:
            import colab
            pyenv = "google_colab"
        except:
            try:
                aux = __file__
                pyenv = "python"
            except:
                print("Not in python")
                pyenv = "jupyter_notebook"
        # Check the version for python
        try:
            import platform
            python_version = platform.python_version()
        except:
            python_version = ""
        # Check the version for numpy library
        try:
            from numpy import version as numpy_version
            numpy_version = numpy_version.version
        except:
            numpy_version = ""
        # Check the version for matplotlib pyplot
        try:
            from matplotlib import __version__ as plt_version
        except:
            plt_version = ""
        # Pack and return
        configuration = {
                         "environment":pyenv,
                         "python_version":python_version,
                         "GenericSimulationLibrary_version":GSL_version,
                         "numpy_version":numpy_version,
                         "matplotlib_version":plt_version,
                         }
        return configuration

    def status(self):
        """Prints out the detected configuration: environment, python and library versions.
        """
        # Configuration
        print("System configuration:")
        for key in self.configuration:
            library = "    " + key.replace("_", " ") + ":"
            if self.configuration[key]:
                print(library, self.configuration[key])
            else:
                print(library, "Not installed")
        # Inputs
        print("Inputs:")
        if self.inputs:
            for key in self.inputs:
                print("    "+key, self.inputs[key])
        else:
            print("    No inputs")
        # plot_options
        print("plot_options:")
        if self.plot_options:
            for key in self.plot_options:
                print("    "+key, self.plot_options[key])
        else:
            print("    No plot_options")
        return  

    def new(self, inputs, plot_options=None):
        """Associates inputs and plot options to the simulation. 

        :param inputs: The inputs that will be used in the simulation. 
            This can be completely personalized. 
        :type inputs: dict
        :param plot_options: The plot options, defaults to None
        :type plot_options: dict, optional
        """
        self.inputs = inputs
        self.plot_options = plot_options

    def save(self, filename):
        """Saves the current state of the simulation, with all
        the provided information. The created file can be
        used with the `load` method to restore the simulation. 

        :param filename: Name for the simulation file.
        :type filename: string
        """
        # Pickle and return
        my_dict = {
                   "configuration":self.configuration,
                   "inputs":self.inputs, 
                   "outputs":self.outputs,
                   "plot_options":self.plot_options,
                  }
        with open(filename, "wb") as fh:
            pickle.dump(my_dict, fh)
            print("Saving simulation into file ", filename)         
        self.download(filename)  #Offer to download the file 
        return

    def load(self, filename):
        """Loads a simulation from a simulation file generated
        with the `save` method to restore the simulation. 

        :param filename: Name for the simulation file.
        :type filename: string
        """
        # Unpack and assign
        with open(filename, "rb") as f:
            my_dict=pickle.load(f)
        self.configuration=my_dict["configuration"]
        self.inputs=my_dict["inputs"] 
        self.outputs=my_dict["outputs"] 
        self.plot_options=my_dict["plot_options"]
        return

    def simulate(self):
        """Conditionally imports the numpy library.
        """
        if self.configuration["numpy_version"]:
            from .simulation_code import execute_simulation
        else:
            print("Cannot simulate - numpy library not installed.")
            return
        # Unpack required values
        x_min = self.inputs["x_min"]
        x_max = self.inputs["x_max"]
        N_points = self.inputs["N_points"]
        m = self.inputs["m"]
        b = self.inputs["b"]
        # Run the delegated simulation
        outputs = execute_simulation(x_min, x_max, N_points, m, b)
        # Store simulation
        self.outputs = outputs
        return
    
    def plot(self, filename="", display=True):
        """Conditionally imports the matplotlib library,
        and if possible, plots the experimental data given
        in plot_options, and the simulation data.
        
        :param filename: Filename to save the graph. If not provided, figure is not saved. Defaults to ''.
        :type filename: str, optional
        :param display: Boolean to show (True) or not show (False) the graph. Defaults to False
        :type display: bool, optional
        """
        if self.configuration["matplotlib_version"]:
            from matplotlib import pyplot as plt    
        else:
            print("Cannot plot - matplotlib library not installed.")
            return
        # Create the figure
        my_fig = plt.figure(figsize=(16,8))
        has_content = False
        # Add the simulation, if possible
        if "x" in self.outputs and "y" in self.outputs:
            x = self.outputs["x"]
            y = self.outputs["y"]
            plt.plot(x, y, **self.plot_options["sim_kwargs"])
            has_content=True
        # Add the (experimental) plot_options, if possible
        if "data_x" in self.plot_options and "data_y" in self.plot_options:
            plt.plot(self.plot_options["data_x"], 
                     self.plot_options["data_y"], 
                     **self.plot_options["data_kwargs"],
            )
            has_content=True
        plt.legend()
        # Add the properties
        if "xlabel" in self.plot_options:
            plt.xlabel(self.plot_options["xlabel"])
        if "ylabel" in self.plot_options:
            plt.ylabel(self.plot_options["ylabel"])
        if "title" in self.plot_options:
            plt.title(self.plot_options["title"])
        # Save figure, if filename provided
        if filename:
            my_fig.savefig(filename)
        # Show figure, if asked for
        if display:
            if has_content:
                plt.show()
            else:
                print("No content to plot.")
        plt.close()
        return

    def export_xlsx(self, filename):
        """Creates an excel file and saves
        the plot data and simulation data.
        It helps providing a file format
        that final users might be more familiar with.        

        :param filename: Name for the file.
        :type filename: string
        """

        # Create the file
        with open(filename, "w") as fh:
            fh.write("Este es un test\n")
            fh.write("TEST")
            print("Exported simulation as xlsx into file", filename)
        self.download(filename)  #Offer to download the file 
        
    def download(self, filename):
        """Utility to download file, using colab
        """
        if self.configuration["environment"]=="google_colab":
            from google.colab import files
            files.download(filename)
        return

def test(iot1, o2p):
    """[summary]

    :param iot1: [description]
    :type iot1: [type]
    :param o2p: [description]
    :type o2p: [type]
    """
