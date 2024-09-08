import matplotlib.pyplot as plt
import math

# Dibuja la evolución del área optenida por los algotimos
def plot_area(opti = False) :
    if not opti : f = open("./Data/Solutions/eigenvalarea.in", "r")
    else    : f = open("./Data/Solutions/eigenvalareaopti.in", "r")
    lines = f.readlines()
    x = []
    y = []
    for l in lines : 
        s = list(map(float, l.split()))
        x.append(s[0])
        y.append(s[2])
    f.close()

    if not opti : g = open("./Data/Solutions/maxareaoriginal.in", "r")
    else    : g = open("./Data/Solutions/maxareaoriginalopti.in", "r")
    lines = g.readlines()
    t = []
    z = []
    for l in lines : 
        s = list(map(float, l.split()))
        t.append(s[0])
        z.append(s[1])
    g.close()

    color = "blue" if not opti else "cyan" 
    label = "Curvas con $L(ξ) = 4\pi^2$" + (" con optimización" if opti else "")
    plt.plot(x, y, 'b-o', markersize = 4, label = label, color = color)
    color = "green" if not opti else "lime" 
    label = "Curvas con $\sigma(ξ) = 2\pi$" + (" con optimización" if opti else "")
    plt.plot(t, z, 'g-o', markersize = 4, label = label, color = color)



fig = plt.figure(figsize = (8,5))
plt.title("Evolución del área máxima")
plt.xlabel("Grado de la curva $n$")
plt.ylabel("Área")
plt.plot([0, 40], [math.pi, math.pi], '--', color = "orange", linewidth = 2.5,label = "$\pi$")
plot_area()
plot_area(True)
plt.legend()
plt.show()
