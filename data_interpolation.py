import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
origin = 'lower'
data = np.loadtxt('DATI.DAT')
x = np.linspace(200.,650.,9)
y= np.linspace(10.,30.,15)
# xmin=data(0).min
# xmax=data(0).max
# ymin=data(1).min
# ymax=data(1).max
# Resample your data grid by a factor of 3 using cubic spline interpolation.
data = scipy.ndimage.zoom(data, 3)


CS=plt.contourf(x,y,data,100)
plt.rcParams['contour.negative_linestyle'] = 'solid'
CS2 = plt.contour(CS, levels=CS.levels[::10],
                  colors='k',
                  origin=origin,
                  hold='on')
plt.clabel(CS2, fontsize=9, inline=1)
plt.axis([200, 650, 10, 30])
plt.colorbar(CS)

plt.show()