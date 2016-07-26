import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
origin = 'lower'
#def func(x, y):
#     return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2


grid_x, grid_y = np.mgrid[200:650:100j, 10:30:100j]
data = np.loadtxt( 'Mappa.txt', usecols = (0,1,2))
points=(data[:,0], data[:,1])
values=(data[:,2])

#values = np.loadtxt('DATI2.DAT')
grid_z0 = griddata(points, values, (grid_x, grid_y), method='cubic')

CS=plt.contourf(grid_x,grid_y,grid_z0,100)
plt.rcParams['contour.negative_linestyle'] = 'solid'
CS2 = plt.contour(CS, levels=CS.levels[::10],
                  colors='k',
                  origin=origin,
                  hold='on')
plt.clabel(CS2, fontsize=9, inline=1)
#plt.axis([200, 650, 10, 30])
plt.colorbar(CS)
plt.show()