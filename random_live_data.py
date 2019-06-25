import time
import os
import sys
from scipy.constants import pi
import numpy as np

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect number of arguments enter period and noise of sine wave.")
        sys.exit(1)

    period = np.float(sys.argv[1])
    noise = np.float(sys.argv[2])


    #Set up data file generation
    filename = "test_live_data.dat"
    dt = 1.0 #s
    s = lambda t: np.sin((2*pi/period)*t)
    

    while True:
        
        #Generate sine wave amplitude data and save to file ever delta t
        t = time.time()
        a = s(t)*(1.0+np.random.normal(0,scale=noise))
        time.sleep(dt)
        try:
            if not os.path.isfile(filename):
                f = open(filename,'w')
                f.write('%f\t%f\n'%(t,a))
                f.close()
            else:
                f = open(filename,'a')
                f.write('%f\t%f\n'%(t,a))
                f.close()
        except KeyboardInterrupt:
            print("Exiting.")
            sys.exit(0)

       
