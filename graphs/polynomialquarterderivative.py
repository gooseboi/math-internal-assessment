#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

def f_0(x):
    return x**2

def f_1(x):
    return x + 1

def f_2(x):
    return x + 2

def f_3(x):
    return x

def f_4(x):
    return 2*x

if __name__ == '__main__':
    x = np.linspace(0, 10, 300)
    plt.plot(x, f_0(x), linestyle="solid", label=r"$x^2$", color='blue')
    plt.plot(x, f_1(x), linestyle="dashed", label=r"$D^\frac{1}{4}x^2$", color='green')
    plt.plot(x, f_2(x), linestyle="dashed", label=r"$D^\frac{2}{4}x^2$", color='orange')
    plt.plot(x, f_3(x), linestyle="dashed", label=r"$D^\frac{3}{4}x^2$", color='cyan')
    plt.plot(x, f_4(x), linestyle="solid", label=r"$2x$", color='red')
    plt.legend(fontsize=13)
    plt.grid()
    plt.xlabel(r"$\mathdefault{x}$", math_fontfamily="cm")
    plt.ylabel(r"$\mathdefault{y}$", rotation=0, math_fontfamily="cm")

    plt.savefig(sys.argv[1], format='pdf')
