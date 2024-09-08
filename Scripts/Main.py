from Bezier import Bezier
import matplotlib.pyplot as plt
import numpy as np

delta = 0.01

# Construye y dibuja una curva de Bézier a partir de sus puntos de control
def plot_curve(points, show = True, save = False) :
    t_points = np.arange(0, 1+delta, delta)
    curve = Bezier.bezier_curve(t_points, points) 
    print(points[:, 0])
    if show : plt.figure(figsize = (5,5))
    plt.plot(curve[:, 0], curve[:, 1], "blue")
    plt.plot(points[:, 0], points[:, 1], 'ro--', markersize = 4, linewidth = 0.7)
    if save : plt.savefig("SolucionOrig" + str(len(points)) + ".png")
    if show : plt.show()

# Devuelve los puntos de control de un fichero de ejemplo
def read_test_points(id) :
    fname = "./Data/Test/test" + str(id) + ".in"
    f = open(fname, "r")
    p = int(f.readline())
    points = []
    for _ in range(p) :
        line = f.readline().split()
        x = float(line[0]); y = float(line[1])
        points.append([x, y])
    points = np.array(points)
    print(points)
    f.close()
    return points

# Dibuja los ejemplos
def print_examples() :
    for id in range(1,10) :
        points = read_test_points(id)
        plot_curve(points)

# Dibuja un ojo a partir de curvas de Bézier
def print_eye() :
    fname = "eye.in"
    f = open(fname, "r")
    plt.figure(figsize = (5,5))
    for _ in range(6) :
        n = int(f.readline())
        print("Aqui", n)
        points = []
        for i in range(n) :
            line = f.readline().split()
            x = float(line[0]); y = float(line[1])
            points.append([x, y])
        points = np.array(points)
        plot_curve(points, show = False)
    f.close()
    plt.show()

# Dibuja Lump a partir de curvas de Bézier
def print_dog() :
    fname = "dog.in"
    f = open(fname, "r")
    plt.figure(figsize = (8,5))
    for _ in range(9) :
        n = int(f.readline())
        points = []
        for i in range(n) :
            line = f.readline().split()
            x = float(line[0]); y = float(line[1])
            points.append([x, y])
        points = np.array(points)
        plot_curve(points, show = False)
    f.close()
    plt.show()

def check_curve(n, name) :
    fname = ".Data/" + name + str(n) + ".in" 
    f = open(fname, "r")
    t = int(f.readline())
    points = []
    for _ in range(t) :
        line = f.readline().split()
        x = float(line[0]); y = float(line[1])
        points.append([x, y])
    points = np.array(points)
    print(points)
    plot_curve(points, save = True)
    f.close()



##############################
# LLAMAR A LO QUE SE NECESTE #
##############################


points1 = read_points(11)
points2 = read_points(12)
plot_curve(points1)
plot_curve(points2)

#for i in range(3, 11) :
    #check_curve(i, "Iso/iso")
    #check_curve(i, "Orig/orig")
    #check_curve(i, "Opt/opt")