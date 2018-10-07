import numpy as np
import matplotlib.pylab as plt

def printHello():
    print("hello, World!")

def mkSinGraph():
    c_i = 50
    q = 0.4
    V = 2
    t = np.linspace(0, 60, 100)
    line = c_i * (1 - np.exp(-t * q / V))
    plt.rcParams.update({'font.size': 12})
    plt.figure()
    plt.title('Exit Concentration as a Function of Time')
    plt.plot( t ,  line )
    plt.xlabel('$t\; [min]$')
    plt.ylabel('$c(t) \; [kg/m^{3}]$')
    plt.show()

def main():
    printHello()
    mkSinGraph()

if __name__ == "__main__":
    main()
    exit(0)
