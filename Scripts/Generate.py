import random

# Genera una nube de puntos aleatorios
def generate_points(n, max, i) :
    points = []
    for _ in range(n) :
        x = random.uniform(0, max)
        y = random.uniform(0, max)
        points.append([x, y])
    
    file_name = "./Data/Random/random" + str(i) + ".in"
    f = open(file_name, "w")
    f.write(str(n) + "\n")
    for p in points:
        f.write(str(p[0]) + " " + str(p[1]) + "\n")
    f.close()

for i in range(1, 11) :
    generate_points(50, 50.0, i)
