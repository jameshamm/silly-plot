"""The code for any sort of plotting is located here. """

import numpy as np
import matplotlib.pyplot as plt


def get_input():
    while True:
        line = input()
        if line in ("quit", "q", "c_q"):
            print("Exiting now")
            yield None
        yield line


def is_command(line):
    return line == "meh"


def to_data(line):
    try:
        x, y = line.split()
        x, y, map(float, (x, y))
    except Exception as e:
        print("Received an exception")
        print(e)
        return None
    else:
        return x, y


def run_plotter(args):
    plt.axis([0, 10, 0, 1])
    plt.ion()
    plt.pause(0.001)

    # Main waiting loop
    line = input()
    while line not in ("quit", "q", "cq"):
        print("GOT", line)
        if is_command(line):
            # execute the command
            print("Got command", line)         
        else:
            data = to_data(line)
            if data is None:
                print("Unrecognised line? It was ignored.")
            else:
            # plot the data on the screen
                x, y = data
                plt.scatter([x], [y])
                plt.draw()
                print("Plotted", x, y)
        line = input()
    
    print("STOPPED WITH", line)
    plt.ioff()
    if line == "cq":
        print("leave")
        # Completely quit
        return

    # Block so the figure stays
    plt.show()
