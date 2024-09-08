# Calcula los coeficientes de una curva de Bézier
import numpy as np
class Bezier() :
    def interpolate(t, P1, P2) : # interpola 2 puntos
       # print(t, P1, P2, (1-t)*P1 + t*P2)
        return (1 - t) * P1 + t * P2

    def bezier_point(t, points) : # calcula B(t)
        n = len(points) - 1
        beta = points.copy()
        for j in range(1, n + 1) :
            for i in range(n-j+1) :
                beta[i] = Bezier.interpolate(t, beta[i], beta[i+1])
        return beta[0]

    def bezier_curve(t_values, points) : # puntos de la curva
        dim = len(points[0])
        curve = []
        for t in t_values :
            #print(Bezier.bezier_point(t, points))
            curve.append(Bezier.bezier_point(t, points))
        #for i in curve : print(i)
        return np.array(curve)
