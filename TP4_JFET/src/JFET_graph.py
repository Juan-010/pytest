from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline

x = [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20]
x_new= np.linspace(0, 20, 300)
colors = ['r','g','c','m','b']
y1 = [0, 5.7, 9.4, 10.8, 11.4, 11.55, 11.71, 11.71, 11.71, 11.71, 11.71, 11.71, 11.71, 11.71] 
y2 = [0, 4.7, 7.5, 8.7, 9, 9.2, 9.3, 9.3, 9.4, 9.3, 9.2, 9.2, 9.1, 9.1]
y3 = [0, 4.7, 6.9, 7.8, 8.1, 8.1, 8.3, 8.4, 8.4, 8.4, 8.4, 8.3, 8.3, 8.2]
y4 = [0, 1.8, 3.9, 4.2, 4.4, 4.5, 4.6, 4.6, 4.6, 4.6, 4.7, 4.7, 4.5, 4.6]
y5 = [0, 1.9, 2.2, 2.4, 2.5, 2.5, 2.6, 2.6, 2.6, 2.7, 2.7, 2.7, 2.7, 2.7]
stability_curve = [[0, 1, 2, 3, 4, 30], [0 ,y5[1], y4[2], y1[3], 40, 40]] 
values = []
values.append([x, y1, 0])
values.append([x, y2, 1])
values.append([x, y3, 2])
values.append([x, y4, 3])
values.append([x, y5, 4])
smooth_values = []
smooth_values.append([x_new, make_interp_spline(x, y1, k=3)(x_new), 0])
smooth_values.append([x_new, make_interp_spline(x, y2, k=3)(x_new), -0.25])
smooth_values.append([x_new, make_interp_spline(x, y3, k=3)(x_new), -0.44])
smooth_values.append([x_new, make_interp_spline(x, y4, k=3)(x_new), -1.47])
smooth_values.append([x_new, make_interp_spline(x, y5, k=3)(x_new), -1.94])

for i in range(5):
    plt.plot(smooth_values[i][0], smooth_values[i][1], color = colors[i] , label=r"I$_D$ @ V$_{GS} =$ " + str(smooth_values[i][2]) + r'V')
    
for i in range(5):
    plt.plot(values[i][0], values[i][1], color = colors[i], linestyle = 'None',marker='.', markersize=10.0)
#plt.plot(stability_curve[0], stability_curve[1])
plt.xlabel(r'V$_{DS}$[V]', loc='right')
plt.ylabel(r'I$_{D}$ [mA]', loc='top')
plt.title('Curvas basadas en las mediciones')
plt.grid(linestyle='--')
plt.ylim(0, 20)
plt.xlim(0, 20)
plt.legend(loc='best')
plt.fill_between(stability_curve[0], stability_curve[1], 0, facecolor = 'red', alpha=0.2)
plt.fill_between(stability_curve[0], stability_curve[1], 30, facecolor = 'green', alpha=0.2)
plt.text(6, 15.5, 'Región de \nSaturación')
plt.text(0.5, 15.5, 'Región\nLineal')
#plt.show()
plt.savefig('P3_Curvas.pdf')
