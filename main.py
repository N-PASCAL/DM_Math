import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
def PrintMatrix(M):
    for ligne in M:
        print(" ".join(str(val) for val in ligne)) 

 
# TP 1 | Question 1    
print("TP 1 | Question 1\n")

def transpose(M):
    rows = len(M)      
    cols = len(M[0]) 
    
    T = [[0] * rows for k in range(cols)]

    for i in range(cols):      
        for j in range(rows):
            T[i][j] = M[j][i]  
    return T

M = [
        [0,1],
        [2,1],
        [-1,3]
    ]

PrintMatrix(M)
print()
PrintMatrix(transpose(M))
print()


# TP 1 |  Question 2
print("TP 1 | Question 2\n")
def ligne(n,xmin,xmax):
    W=[]
    dx=(xmax-xmin)/(n-1)
    for x in range (n):
        W.append([x*dx,0,0])
    return(transpose(W))

def PrintLigne():
    (X,Y,Z)=ligne(20,-5,5)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(X, Y, Z, c=Z, cmap='ocean');
    plt.show()

PrintLigne()
print()


# TP 1 | Question 3
print("TP 1 | Question 3\n")
def VoidSquare(n, a):
    W = []  
    c = a / 2  
    pointsByCote = max(n // 4, 1)  # Nombre de points par côté (au moins 1)
    
    # Générer les points sur chaque côté
    for i in range(pointsByCote):
        if pointsByCote > 1:
            t = i / (pointsByCote - 1) 
        else:
            t = 0  

        # Côté haut (de gauche à droite)
        W.append([-c + t * a, c, 0])
        # Côté droit (de haut en bas)
        W.append([c, c - t * a, 0])
        # Côté bas (de droite à gauche)
        W.append([c - t * a, -c, 0])
        # Côté gauche (de bas en haut)
        W.append([-c, -c + t * a, 0])

    return transpose(W) 


def PrinteVoidSquare(n, a):
    X, Y, Z = VoidSquare(n, a)  

    fig = plt.figure()  
    ax = fig.add_subplot(111, projection='3d')  
    ax.scatter(X, Y, Z, c='b', marker='o')  

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Carré Vide en 3D")

    plt.show()  

PrinteVoidSquare(20, 4)  
print()

# TP 1 | Question 4
print("TP 1 | Question 4\n")
def Square(n, a):
    W = []  
    pointsByCote = int(n**0.5)  
    if pointsByCote < 1:  
        pointsByCote = 1
    
    pas = a / (pointsByCote - 1) if pointsByCote > 1 else 0  

    for i in range(pointsByCote):
        for j in range(pointsByCote):
            x = -a/2 + i * pas  
            y = -a/2 + j * pas  
            W.append([x, y, 0])  

    return transpose(W)  

def PrintSquare(n, a):
    X, Y, Z = Square(n, a)  

    fig = plt.figure()  
    ax = fig.add_subplot(111, projection='3d')  
    ax.scatter(X, Y, Z, c='b', marker='o')  

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Carré Plein en 3D")

    plt.show() 
    
PrintSquare(20, 4)
print()


# TP 1 | Question 5
print("TP 1 | Question 5\n")
def Paving(n, a, b, c):
    
    W = []  
    pointsByCote = int(n ** (1/3))  
    if pointsByCote < 1:  
        pointsByCote = 1

    # Pas entre les points sur chaque axe
    pas_x = a / (pointsByCote - 1) if pointsByCote > 1 else 0
    pas_y = b / (pointsByCote - 1) if pointsByCote > 1 else 0
    pas_z = c / (pointsByCote - 1) if pointsByCote > 1 else 0

    for i in range(pointsByCote):  # Axe X
        for j in range(pointsByCote):  # Axe Y
            for k in range(pointsByCote):  # Axe Z
                x = -a / 2 + i * pas_x
                y = -b / 2 + j * pas_y
                z = -c / 2 + k * pas_z
                W.append([x, y, z])
    return transpose(W)  

def PrintPaving(n, a, b, c):
    X, Y, Z = Paving(n, a, b, c)  

    fig = plt.figure() 
    ax = fig.add_subplot(111, projection='3d')  
    ax.scatter(X, Y, Z, c='g', marker='o')  
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Pavé Plein en 3D")

    plt.show()  

PrintPaving(100, 4, 2, 3)  
print()


# TP 1 | Question 6
print("TP 1 | Question 6 A\n")
def factoriel(n):
    if n == 0:
        return 1  
    
    resultat = 1
    for i in range(1, n + 1):  
        resultat *= i
    
    return resultat
    
print(factoriel(5))

print()


print("TP 1 | Question 6 B\n")
def cosinus(x):
    """Approximation de cos(x) en utilisant le développement limité d'ordre 6."""
    return 1 - (x**2 / factoriel(2)) + (x**4 / factoriel(4)) - (x**6 / factoriel(6))

def sinus(x):
    """Approximation de sin(x) en utilisant le développement limité d'ordre 7."""
    return x - (x**3 / factoriel(3)) + (x**5 / factoriel(5)) - (x**7 / factoriel(7))


x = 0.5  
print(f"Approximation de cos({x}) : {cosinus(x):.6f}")
print(f"Approximation de sin({x}) : {sinus(x):.6f}")

print()


print("TP 1 | Question 6 C\n")
def Circle(n, R):
    W = []
    nbCircle = int(np.sqrt(n))  
    nbPointByCircle = max(n // nbCircle, 1)  
    
    for i in range(nbCircle):
        r = (i / (nbCircle - 1)) * R if nbCircle > 1 else R
        for j in range(nbPointByCircle):
            theta = (j / nbPointByCircle) * 2 * np.pi
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            W.append([x, y, 0])

    return np.array(W).T  

def PrintCircle(n, R):
    X, Y, Z = Circle(n, R)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z, c='r', marker='o')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect([1,1,1]) 
    ax.set_title("Cercle Plein en 3D")

    plt.show()

PrintCircle(500, 50)

print()

print("TP 1 | Question 7\n")
def Cylinder(n, R, h):
    W = []
    nbCircles = int(np.sqrt(n)) 
    nbPointByCircles = max(n // nbCircles, 1) 
    
    # Surface latérale
    for i in range(nbCircles):
        z = -h / 2 + (i / (nbCircles - 1)) * h if nbCircles > 1 else 0
        for j in range(nbPointByCircles):
            theta = (j / nbPointByCircles) * 2 * np.pi
            x = R * np.cos(theta)
            y = R * np.sin(theta)
            W.append([x, y, z])

    # Base supérieure et inférieure
    for z in [-h/2, h/2]:
        for j in range(nbPointByCircles):
            r = (j / nbPointByCircles) * R
            theta = (j / nbPointByCircles) * 2 * np.pi
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            W.append([x, y, z])

    return np.array(W).T  

def PrintCylinder(n, R, h):
    X, Y, Z = Cylinder(n, R, h)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z, c='b', marker='o')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect([1,1,2])  

    ax.set_title("Cylindre Plein en 3D")
    plt.show()

PrintCylinder(1000, 30, 60)
print()

##################################################################
######  Fin du TP 1
##################################################################

