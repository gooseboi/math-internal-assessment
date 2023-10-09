#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

def f_0(x):
    off=(0/4)*(np.pi/2)
    return np.sin(x + off)

def f_1(x):
    off=(1/4)*(np.pi/2)
    return np.sin(x + off)

def f_2(x):
    off=(2/4)*(np.pi/2)
    return np.sin(x + off)

def f_3(x):
    off=(3/4)*(np.pi/2)
    return np.sin(x + off)

def f_4(x):
    off=(4/4)*(np.pi/2)
    return np.sin(x + off)

if __name__ == '__main__':
    x = np.linspace(0, 2*np.pi, 300)
    ax = plt.plot(x, f_0(x), color='blue', label=r"$\sin{x}$")
    plt.plot(x, f_1(x), color='green', linestyle='dashed', label=r"$D^\frac{1}{4}\sin{x}$")
    plt.plot(x, f_2(x), color='orange', linestyle='dashed', label=r"$D^\frac{2}{4}\sin{x}$")
    plt.plot(x, f_3(x), color='cyan', linestyle='dashed', label=r"$D^\frac{3}{4}\sin{x}$")
    plt.plot(x, f_4(x), color='red', label=r"$\cos{x}$")
    plt.legend()
    plt.grid()
    plt.xlabel(r"$\mathdefault{x}$", math_fontfamily="cm")
    plt.ylabel(r"$\mathdefault{y}$", rotation=0, math_fontfamily="cm")

    plt.savefig(sys.argv[1], format='pdf')
