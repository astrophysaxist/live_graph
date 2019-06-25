import os
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

def graph(frame, filename):
    """Graphs data from given file"""
    if not os.path.isfile(filename):
        print("Filename %s does not exist Exiting."%filename)
        sys.exit(1)
    data = np.genfromtxt(filename, unpack=True)
    time = data[0]
    amp = data[1]
    ax.clear()
    ax.plot(time, amp, 'bx')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    plt.title('Live %s'%filename)



if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect number of arguments. Please provide file to watch and duty cycl to updat graph.")
        sys.exit(1)

    filename = sys.argv[1]
    duty_cycle = np.float(sys.argv[2]) #ms

    #Open figure and subplot axes
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)

    ani = animation.FuncAnimation(fig, func=graph,fargs=[filename], interval=duty_cycle)
    plt.show()
