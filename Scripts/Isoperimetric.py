from numpy import linalg as LA
import numpy as np
import math

MAXN = 500

# Números combinatorios
comb = [[0 for j in range(MAXN)] for i in range(MAXN)]
comb[0][0] = 1
for i in range(1,MAXN) :
    for j in range(i+1) :
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

# Calcula la matriz A
def compute_matrixA(n) :
    A = [[0 for j in range(n-1)] for i in range(n-1)]
    for x in range(n-1) :
        i = x+1
        for y in range(x+1, n-1) :
            k = y+1
            b1 = comb[i+k-1][k]
            b2 = comb[2*n-1-k-i][n-1-k]
            A[x][y] = (k-i)*b1*b2 / (i*(n-k))
            A[y][x] = -A[x][y]
    for i in range(n-1) :
        assert A[i][i] == 0

    for i in range(n-1) :
        for j in range(n-1) :
            assert A[i][j] == -A[j][i]
    return A

# Calcula la matriz B
def compute_matrixB(n) :
    B = [[0 for j in range(n-1)] for i in range(n-1)]
    for x in range(n-1) :
        i = x+1
        for y in range(n-1) :
            k = y+1
            b1 = comb[i+k-2][i-1]
            b2 = comb[2*n-2-i-k][n-1-i]
            B[x][y] = b1*b2*(2*(n-1)*i*k-n*(i**2+k**2-i-k)) / (i*k*(n-i)*(n-k))
    for i in range(n-1) :
        for j in range(n-1) :
            assert B[i][j] == B[j][i]
    return B


# Genera las matrices del haz
def generate_pencil(n) :
    A = compute_matrixA(n)
    B = compute_matrixB(n)
    C = [[0 for j in range(2*n-2)] for i in range(2*n-2)]
    D = [[0 for j in range(2*n-2)] for i in range(2*n-2)]
    coefC = n / (4*comb[2*n-1][n])
    for x in range(n-1) :
        for y in range(n-1, 2*n-2) :
            C[x][y] = coefC * A[x][y-n+1]
    for x in range(n-1, 2*n-2) :
        for y in range(n-1) :
            C[x][y] = coefC * A[y][x-n+1]
    coefD = n * (n-1) / comb[2*n-1][n]
    for x in range(n-1) :
        for y in range(n-1) :
            D[x][y] = coefD * B[x][y]
            D[x+n-1][y+n-1] = D[x][y]
    return np.asmatrix(C), np.asmatrix(D)
    
# Guarda una curva solución del problema 
def save_curve(n, x, y, path) :
    xt = np.transpose(x)
    yt = np.transpose(y)
    B = compute_matrixB(n)
    coef = n * (n-1) / comb[2*n-1][n]
    den = np.matmul(np.matmul(xt, B), x).item(0) + np.matmul(np.matmul(yt, B), y).item(0)
    den = math.sqrt(coef * den)
    px = [0] * (n-1)
    py = [0] * (n-1)
    for i in range(n-1) :
        px[i] = l * x[i].item(0) / den
        py[i] = l * y[i].item(0) / den
   
    fname = path + str(n) + ".in"
    file = open(path, "w")
    file.write(str(n+1) + "\n")
    file.write("0 0\n")
    for i in range(n-1) :
        file.write(str(px[i]) + " " + str(py[i]) + "\n")
    file.write("0 0\n")
    file.close()

# Algoritmo que calcula la solución al problema reducido
def solution(n, l) :
    C, D = generate_pencil(n)    
    M = np.matmul(LA.inv(D), C)
    eigval, eigvec = LA.eig(M)
    # Hay que tomar la parte real por los errores de precisión
    eigval = eigval.real
    eigvec = eigvec.real
    maxeigval = np.max(eigval)
    maxid = np.argmax(eigval)
    area = maxeigval * l*l
    precision = 10
    data = open("./Data/Solutions/eigenvalarea.in", "a")
    s = str(n) + " " + str(round(maxeigval, precision)) + " " + str(round(area, precision))
    data.write(s + "\n")
    data.close()
    print("n =", n)
    print("Máximo autovalor =", maxeigval)
    print("Área máxima =", area)
    
    z = eigvec[:,maxid]
    x, y = np.split(z, 2)
    save_curve(n, x, y, "./Data/Iso/iso")

# Algoritmo optimizad que calcula la solución al problema reducido
def solution_optimized(n, l) :
    A = np.asmatrix(compute_matrixA(n))
    B = np.asmatrix(compute_matrixB(n))
    M = np.matmul(LA.inv(B), A)
    M2 = np.matmul(M, M)
    eigval, eigvec = LA.eig(M2)
    eigval = eigval.real
    eigvec = eigvec.real
    minid = np.argmin(eigval)
    mu = -eigval[minid]
    lbda = math.sqrt(mu) / (4*(n-1))
    area = lbda * l*l
    print("Área máxima con la optimización:", area)
    precision = 10
    data = open("./Data/Solutions/eigenvalareaopti.in", "a")
    s = str(n) + " " + str(round(lbda, precision)) + " " + str(round(area, precision))
    data.write(s + "\n")
    data.close()
    y = eigvec[:, minid]
    x = np.matmul(M, y) / math.sqrt(mu)
    save_curve(n, x, y, "./Data/Opt/opt")




###############################
# LLAMAR A LO QUE SE NECESITE #
###############################

# ¡¡¡¡Cuidado con los append en los ficheros de la carpeta Solution. No se sobreescribe lo que hubiera antes!!!!!

l = 2*math.pi
for n in range(3, 41) :
    solution(n, l)
    #solution_optimized(n, l)