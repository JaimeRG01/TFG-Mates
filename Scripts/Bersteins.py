import matplotlib.pyplot as plt
import numpy as np
import math


def plot_berstein(x, n) :
    for i in range(n+1) :
        y = [math.comb(n,i)*(t**i)*(1-t)**(n-i) for t in x]
        s = "$B_" + str(i) + "^" + str(n) + "(t)$"
        plt.plot(x, y, '-', label = s)
    plt.legend()
    plt.title("Grado " + str(n))
    plt.show()

def plot_examples_bezier_curve(t) :
    x = [i for i in t]
    y = [i for i in t]
    plt.plot(x, y, '-', label = "$α_1(t)$")
    plt.plot([0,1], [0,1], 'ro', label = "Puntos de control")
    plt.legend()
    plt.show()
    x = [i*(2-3*i) for i in t]
    y = [i*(i+2) for i in t]
    plt.plot(x, y, '-', label = "$α_2(t)$")
    plt.plot([0,1,-1], [0,1,3], 'ro', label = "Puntos de control")
    plt.legend()
    plt.show()


delta = 0.01
N = 100
x = [i*delta for i in range(N+1)]


plot_examples_bezier_curve(x)

fig = plt.figure(figsize = (5,5))
plot_berstein(x, 2)

fig = plt.figure(figsize = (5,5))
plot_berstein(x, 5)
