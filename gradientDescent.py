# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 09:38:13 2020

@author: RPP
"""

import numpy as np
import matplotlib.pyplot as plt

def gradientDescent(lr, maxEp):
    plt.close()
    plt.clf()
    minx = -5
    maxx = 5
    plotError(minx, maxx)
    
    
    #start GD in the min-max range
    nEp = 0
    x = np.random.rand() * (maxx-minx) + minx
    E = error(x)
    print("Erro 0: %f\t x0: %f" % (E, x))
    plt.plot(x, E, 'bo')
    plt.pause(1)
    
    #iterate GD
    while abs(E) > 10**(-5) and nEp < maxEp:
        xAnt = x
        Eant = E
        dx = -lr * dE_dx(x)
        x += dx
        E = error(x)
        nEp += 1
        print("nEp: %d - Erro: %f\t x: %f" % (nEp, E, x))

        plt.plot(xAnt, Eant, 'bo', x, E, 'ro')
        plt.plot([xAnt, x], [Eant, E], 'b')
        plt.draw()
        #wait = input("Press Enter to continue.")
        plt.pause(1)


def plotError(minx, maxx):
    step = 0.01
    x = np.arange(minx, maxx+step, step)
    E = error(x)
    plt.plot(x, E)
        

def error(x):
    return x ** 2


def dE_dx(x):
    return 2*x

if __name__ == "__main__":
    #gradientDescent(0.1, 20)
    #gradientDescent(1.5, 20)
    gradientDescent(0.3, 20)
    #gradientDescent(1, 20)    
    #gradientDescent(0.5, 20)