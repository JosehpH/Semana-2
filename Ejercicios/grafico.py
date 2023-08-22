import matplotlib.pyplot as plt
import numpy as np

def constante():
    x = [1,2,3,4,5,6,7]
    y= [2,2,2,2,2,2,2]

    plt.plot(x,y,'b')
    plt.xlabel("Entradas")
    plt.ylabel("Pasos")
    plt.title("Orden de complejidad constante O(c)")
    plt.show()

def lineal():
    x = list(range(-7,8))
    y= list(map(lambda e: e*e,x))

    plt.plot(x,y,'b')
    plt.xlabel("Entradas")
    plt.ylabel("Pasos")
    plt.title("Orden de complejidad constante O(c)")
    plt.show()

lineal()