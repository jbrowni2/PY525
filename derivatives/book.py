import numpy as np
import pandas as pd
import math


def f(x):
    return math.exp(math.sin(2*x))

def fprime(x):
    return 2*math.cos(2*x)*math.exp(math.sin(2*x))

def forward(x,h):
    return (f(x+h) - f(x))/h

def central(x,h):
    return (f(x+h/2) - f(x-h/2))/h


def main():
    steps = [1/(10**x) for x in range(1,12)]
    for h in steps:
        x = 0.5
        derivForward = forward(x,h)
        derivCentral =  central(x,h)
        deriv = fprime(x)
        errForward = abs(deriv - derivForward)
        errCentral = abs(deriv - derivCentral)

        print(h, "  ", errForward, "    ", errCentral)



if __name__ == '__main__':
    main()
