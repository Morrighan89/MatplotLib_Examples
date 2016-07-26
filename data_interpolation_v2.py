import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def func(x, y):
     return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2


grid_x, grid_y = np.mgrid[200:650:100j, 10:30:100j]
data = np.loadtxt( 'Mappa.txt', usecols = (0,1,2))
points=(data[:,0], data[:,1])
values=(data[:,2])

#values = np.loadtxt('DATI2.DAT')
grid_z0 = griddata(points, values, (grid_x, grid_y), method='cubic')
print(grid_z0)
plt.contourf(grid_x,grid_y,grid_z0)
plt.show()