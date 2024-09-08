from Bezier import Bezier
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
delta = 0.01
def plot_curve(points, show = True, save = False) :
    t_points = np.arange(0, 1+delta, delta)
    curve = Bezier.bezier_curve(t_points, points) 
    print(points[:, 0])
    if show : plt.figure(figsize = (5,5))
    plt.plot(curve[:, 0], curve[:, 1], "blue")
    plt.plot(points[:, 0], points[:, 1], 'ro--', markersize = 4, linewidth = 0.7)
    # plt.grid()
    if save : plt.savefig("SolucionOrig" + str(len(points)) + ".png")
    if show : plt.show()


def read_points(id) :
    fname = "test" + str(id) + ".in"
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

def print_examples() :
    for id in range(1,10) :
        points = read_points(id)
        plot_curve(points)


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


def print_dog() :
    fname = "dog.in"
    f = open(fname, "r")
    plt.figure(figsize = (8,5))
    for _ in range(9) :
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
def print_Q() :
    fname = "letterQ.in"
    f = open(fname, "r")
    plt.figure(figsize = (5,5))
    for _ in range(1) :
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

#print_examples()
#print_eye()
#print_dog()
#print_Q()

#plt.rcParams['figure.figsize'] = [5,5]
#fig, ax = plt.subplots()
ax = None

def animate(t) :
    fname = "iso" + str(t) + ".in"
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




limit = 40
#ani = animation.FuncAnimation(fig, animate, [i for i in range(4,limit)], init_func=animate(3), interval=100)
#plt.show()
#ani.save("isoperimetric.gif")

def check_curve(n, name) :
    fname = name + str(n) + ".in" 
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




points1 = read_points(11)
points2 = read_points(12)
plot_curve(points1)
plot_curve(points2)

#for i in range(3, 11) :
    #check_curve(i, "iso")
    #check_curve(i, "orig")
    #check_curve(i, "opt")