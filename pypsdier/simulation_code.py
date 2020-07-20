import numpy as np
import time
import sys

def execute_simulation(x_min, x_max, N_points, m, b):
    """Function that encapsulates the numerical simulation.

    :param x_min: Lower bound for x
    :type x_min: float (or int)
    :param x_max: Upper bound for y
    :type x_max: flot (or int)
    :param N_points: Number of discretization points.
    :type N_points: int
    :param m: Slope of line
    :type m: flot (or int)
    :param b: Intercept of line
    :type b: float (or int)
    :return: Dictionary with the results of the simulation
    :rtype: dict
    """
    # Simulation
    x = np.linspace(x_min, x_max, num=N_points)
    y = m*x + b
    # Some waiting, just for ilustration purposes
    for t in range(1,13):
        time.sleep(0.1)
        sys.stdout.write("\rElapsed time: %03d secondss %s" %(t, ""))
        sys.stdout.flush()
    sys.stdout.write("\rElapsed time: %03d seconds %s" %(t, "\n"))
    # Pack the outputs
    outputs = {"x":x, "y":y}
    return outputs