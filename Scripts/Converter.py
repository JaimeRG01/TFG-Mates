import numpy as np
import scipy.integrate as integrate
import math

# Obtiene los puntos de un fichero (misma función que en Main)
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
    #print(points)
    f.close()
    return points

# Evalúa la derivada en t
def eval_derivate(t, n, coords) :
    res = 0.0
    for i in range(n) :
        b = (t**i) * ((1-t)**(n-1-i))*math.comb(n-1,i)
        ev = n*(coords[i+1]-coords[i])*b
        res += ev
    return res

# Evalúa bezier en t
def eval_bezier(t, n, coords) :
    res = 0.0
    for i in range(n+1) :
        b = (t**i) * ((1-t)**(n-i))*math.comb(n,i)
        res += b*coords[i]
    return res

# Evalúa el integrando de sigma en t
def sigma_integrand(t, n, points) :
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    d1 = eval_derivate(t, n, x)
    d2 = eval_derivate(t, n, y)
    return math.sqrt(d1**2 + d2**2)

# Evalúa el integrando de P en t
def P_integrand(t, n, points) :
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    d1 = eval_derivate(t, n, x)
    d2 = eval_bezier(t, n, y)
    return d1 * d2

# Obtiene las áreas del fichero name
def get_max_areas(name) :
    f = open(name, "r")
    lines = f.readlines()
    res = []
    for l in lines : 
        s = list(map(float, l.split()))
        res.append(s[2])
    f.close()
    return res




####################################
# UTILIZAR LA RUTA QUE SE NECESITE #
####################################


l = 2*math.pi # longitud


# Si se quiere comprobar el algoritmo optimizado descomentar los ficheros opti y comentar los otros


areas = get_max_areas("./Data/Solutions/eigenvalarea.in") 
#areas = get_max_areas("./Data/Solutions/eigenvalareaopti.in")

g = open("./Data/Solutions/maxareaoriginal.in", "w")
#g = open("./Data/Solutions/maxareaoriginalopti.in", "w")

for i in range(3, 41) :
    points = read_points(i, "./Data/Iso/iso")
    #points = read_points(i, "./Data/Opt/opt")
    n = len(points)-1
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    sigma, error = integrate.quad(sigma_integrand, 0, 1, args = (n, points))
    delta = (l**2) * areas[i-3] / (sigma**2)
    xx = [j * (l / sigma) for j in x]
    yy = [j * (l / sigma) for j in y]

    f = open("./Data/Orig/orig" + str(i) + ".in", "w+")
    #f = open("./Data/Origopt/origopt" + str(i) + ".in", 'w+')

    f.write(str(n+1) + "\n")
    g.write(str(n) + " " + str(round(delta,10)) + "\n")
    for j in range(len(x)) :
        f.write(str(xx[j]) + " " + str(yy[j]) + "\n")
    f.close()
    print("Área de la curva con sigma = 2pi con n = " + str(n) + " ->", round(delta, 10))
g.close()