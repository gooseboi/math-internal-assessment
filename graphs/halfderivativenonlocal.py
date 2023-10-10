#!/usr/bin/env python3

from scipy.integrate import quad
from scipy.special import gamma
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

def f(x):
    if x < 0:
        return 2 * x
    else:
        return x**2 + 3*x + 5

def f_half(t, x):
    return ((x-t)**(-1/2)) * f(t)

def f_half_int(x, a):
    return (1/gamma(1/2)) * quad(lambda t: f_half(t, x), a, x)[0]

def g(x):
    if x < 0:
        return np.sin(x)*x
    else:
        return x**2 + 3*x + 5

def g_half(t, x):
    return ((x-t)**(-1/2)) * g(t)

def g_half_int(x, a):
    return quad(lambda t: g_half(t, x), a, x)[0]

if __name__ == '__main__':
    x_range = np.linspace(-10, 10, 300)
    a_vals = [-2, -5, -10]
    colors = ["red", "blue", "green", "orange", "cyan", "pink"]
    funcs = [[f_half_int, "f"], [g_half_int, "g"]]
    i=0
    for func, name in funcs:
        for a in a_vals:
            f_values = [func(x, a) for x in x_range]
            plt.plot(x_range, f_values, linestyle="solid", label=r"$D^\frac{1}{2}_{%s} (%s)$" % (a, name), color=colors[i])
            i=i+1

    plt.legend(fontsize=13)
    plt.grid()
    plt.xlabel(r"$\mathdefault{x}$", math_fontfamily="cm")
    plt.ylabel(r"$\mathdefault{y}$", rotation=0, math_fontfamily="cm")

    plt.savefig(sys.argv[1], format='pdf')
