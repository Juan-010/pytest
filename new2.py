from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

x1 = [0, 0.25, 0.5, 1, 2, 5, 10, 15]
x2 = [0, 0.25, 0.5, 1, 2, 5, 15]
x3 = [0, 1.25, 2, 5, 10, 15]
x_new= np.linspace(0, 15, 300)
colors = ['r','g','c','m','y']
y1 = [0, 4, 5.04, 5.15, 5.36, 5.56, 5.6, 6.2]
y2 = [0, 6.63, 8.33, 8.55, 8.65, 8.7, 10.1, 11.31]
y3 = [0, 8.5, 10.52, 11.78, 12.19, 12.9, 15]
y3_alt = [0, 8.5, 10.52, 11.78, 12.19, 12.9, 13.9, 15]
y4 = [0, 14.47, 15.3, 16.85, 20.09, 21.78]
y5 = [0, 17.49, 18.16, 20.27, 23.48, 27.71]
value_old = [[x1,y1, 'r'],[x1,y2, 'g'],[x2,y3, 'c'],[x3,y4, 'm'],[x3,y5, 'y']]
values = []
values.append([x_new, make_interp_spline(x1, y1, k=3)(x_new), 15, 'r'])
values.append([x_new, make_interp_spline(x1, y2, k=3)(x_new), 25, 'g'])
values.append([x_new, make_interp_spline(x1, y3_alt, k=3)(x_new), 35, 'c'])
values.append([x_new, make_interp_spline(x3, y4, k=3)(x_new), 45, 'm'])
values.append([x_new, make_interp_spline(x3, y5, k=3)(x_new), 55, 'y'])

for value in values:
    plt.plot(value[0], value[1], color = value[3] , label=r"I$_b =$ " + str(value[2]) + r'$\mu$A')
    
for value in value_old:
    plt.plot(value[0], value[1], color = value[2], linestyle = 'None',marker='.', markersize=10.0)
plt.xlabel(r'V$_{CE}$[V]', loc='right')
plt.ylabel(r'I$_{C}$ [mA]', loc='top')
plt.title('Curvas basadas en las mediciones')
plt.grid(linestyle='--')
plt.ylim(0, 31)
plt.xlim(0, 15)
plt.legend(loc='best')
plt.savefig('potato.pdf')
