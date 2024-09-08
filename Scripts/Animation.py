from Bezier import Bezier
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

plt.rcParams['figure.figsize'] = [5,5]
fig, ax = plt.subplots()
delta = 0.01

# Tomar las curvas que se quieran
# Cambiar también el nombre del gif

#path = "Data/Iso/iso"
#path = "Data/Orig/orig"
#path = "Data/Opt/opt"
path = "Data/Origopt/origopt"

def animate(t) :
    fname = path + str(t) + ".in"
    f = open(fname, "r")
    n = int(f.readline())
    points = []
    for _ in range(n) :
        line = f.readline().split()
        x = float(line[0]); y = float(line[1])
        points.append([x, y])
    points = np.array(points)
    # print(points)
    t_points = np.arange(0, 1+delta, delta)
    curve = Bezier.bezier_curve(t_points, points)
    ax.clear()
    #plt.figure(figsize=(5,5))
    #ax.set_xlim([-3,3])
    #ax.set_ylim([-3,3])
    ax.plot(curve[:,0], curve[:,1])
    ax.plot(points[:, 0], points[:, 1], 'ro--')
    f.close()


limit = 25
ani = animation.FuncAnimation(fig, animate, [i for i in range(4,limit)], init_func=animate(3), interval=100)
plt.show()
#ani.save("./Iso.gif")
#ani.save("./Orig.gif")
#ani.save("./Opt.gif")
ani.save("./Origopt.gif")