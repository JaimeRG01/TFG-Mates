# Para generar nubes de puntos aleatorias

import random
import numpy as np
import matplotlib.pyplot as plt


def generate_points(n, max, i) :
    points = []
    for _ in range(n) :
        x = random.uniform(0, max)
        y = random.uniform(0, max)
        points.append([x, y])
    
    file_name = "random" + str(i) + ".in"
    f = open(file_name, "w")
    f.write(str(n) + "\n")
    for p in points:
        f.write(str(p[0]) + " " + str(p[1]) + "\n")
    f.close()

generate_points(50, 50.0, 2)
