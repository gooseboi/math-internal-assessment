#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

def f_0(x):
    return 2*x + 3

def f_1(x):
    return 2*x + 3

if __name__ == '__main__':
    x = np.linspace(0, 10, 300)
    plt.plot(x, f_0(x), linestyle="solid", label=r"$f'(x)$", color="blue")
    plt.plot(x, f_1(x), linestyle="solid", label=r"$g'(x)$", color = "green")
    plt.legend(fontsize=13)
    plt.grid()
    plt.xlabel(r"$\mathdefault{x}$", math_fontfamily="cm")
    plt.ylabel(r"$\mathdefault{y}$", rotation=0, math_fontfamily="cm")

    plt.savefig(sys.argv[1], format='pdf')
