from Bezier import Bezier
import matplotlib.pyplot as plt
import numpy as np

delta = 0.01

# Construye y dibuja una curva de Bézier a partir de sus puntos de control
def plot_curve(points, show = True, save = False, savename = "") :
    t_points = np.arange(0, 1+delta, delta)
    curve = Bezier.bezier_curve(t_points, points) 
    print(points[:, 0])
    if show : plt.figure(figsize = (5,5))
    plt.plot(curve[:, 0], curve[:, 1], "blue")
    plt.plot(points[:, 0], points[:, 1], 'ro--', markersize = 4, linewidth = 0.7)
    if save : plt.savefig("./Figuras/" + savename + str(len(points)) + ".png")
    if show : plt.show()



# Devuelve los puntos de control de un fichero de ejemplo
def read_points(id, path) :
    fname = path + str(id) + ".in"
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
def print_test_examples() :
    for id in range(1,11) :
        points = read_points(id, "./Data/Test/test")
        plot_curve(points)

# Dibuja los ejemplos generados aleatoriamente
def print_random_examples() : 
    for id in range(1,3) :
        points = read_points(id, "./Data/Random/random")
        plot_curve(points)

# Dibuja un ojo a partir de curvas de Bézier
def print_eye() :
    fname = "./Data/Design/eye.in"
    f = open(fname, "r")
    plt.figure(figsize = (5,5))
    for _ in range(6) :
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

# Dibuja Lump a partir de curvas de Bézier
def print_dog() :
    fname = "./Data/Design/dog.in"
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

# Dibuja una curva obtenida a partir del algoritmo
def check_curve(n, path, name) :
    fname = path + name + str(n) + ".in" 
    f = open(fname, "r")
    t = int(f.readline())
    points = []
    for _ in range(t) :
        line = f.readline().split()
        x = float(line[0]); y = float(line[1])
        points.append([x, y])
    points = np.array(points)
    print(points)
    plot_curve(points, save = True, savename = "Solucion" + name)
    f.close()



###############################
# LLAMAR A LO QUE SE NECESITE #
###############################


print_test_examples()
print_random_examples()

print_dog()
print_eye()


# Contraejemplos
points1 = read_points(11, "./Data/Test/test")
points2 = read_points(12, "./Data/Test/test")
plot_curve(points1)
plot_curve(points2)

# Para representar y guardar las curvas soluciones
#for i in range(3, 11) :
    #check_curve(i, "./Data/Iso/" , "iso")
    #check_curve(i, "./Data/Orig/", "orig")
    #check_curve(i, "./Data/Opt/" ,  opt")