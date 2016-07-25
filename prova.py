import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


(X,Y,Z) = np.loadtxt('prova.DAT')

print(X)
print(X.size)
print(Y)
print(Y.size)
print(Z)
print(Z.size)
Axes3D.plot_surface(X, Y, Z)