from numpy import loadtxt
from scipy.ndimage.filters import gaussian_filter
from matplotlib.pyplot import contour, show

sigma = 0.7 # this depends on how noisy your data is, play with it!
data = loadtxt('dati.txt')
data = gaussian_filter(data, sigma)
contour(data)
show()
from numpy import loadtxt
from scipy.ndimage.filters import gaussian_filter
from matplotlib.pyplot import contour, show

sigma = 0.7 # this depends on how noisy your data is, play with it!
data = loadtxt('data.txt')
data = gaussian_filter(data, sigma)
contour(data)
show()