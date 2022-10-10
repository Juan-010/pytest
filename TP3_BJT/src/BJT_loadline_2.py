from matplotlib import pyplot as plt
import numpy as np
class Point:
    
    def __init__(self, x1, y1, col, label):
        self.x = [x1]
        self.y = [y1]
        self.col = col
        self.lab = label

#2 Pol por Realimentacion
icMax = 2.55
vMax = 12
y = [icMax, 0]
x = [0, vMax]
listop=[]
pt = Point(5.28, 1.43, 'c', r'$\beta_{prom} = 377$')
listop.append(Point(4.96,1.51,"r", r'$\beta = 416$' ))
listop.append(Point(5.33,1.42, "b", r'$\beta = 360$'))
listop.append(Point(5.17,1.46, "g", r'$\beta = 356$'))
listop.append(Point(5.29,1.47, "m", r'$\beta = 367$'))
listop.append(Point(5.1,1.48, "y", r'$\beta = 386$'))
plt.plot(pt.x, pt.y, marker = "o", color = pt.col, markersize = 10.0)
for poi in listop:
    plt.plot(poi.x, poi.y, marker = "o", color = poi.col)
plt.plot(x,y, color = "c")
plt.xlabel(r'V$_{CE}$ [V]', loc='right')
plt.ylabel(r'I$_{C}$ [mA]', loc='top')
plt.title('Recta de Carga por Realimentación')
plt.grid(linestyle='--')
plt.ylim(0, 3)
plt.xlim(0, 13)
plt.savefig('PolRealimentacion.pdf')
#2 Pol por Realimentacion ZOOM
ymin = 1
xmin = 4.25
plt.plot(pt.x, pt.y, marker = "o", color = pt.col, markersize = 10.0, label = pt.lab)
for poi in listop:
    plt.plot(poi.x, poi.y, marker = "o", color = poi.col, label = poi.lab)
plt.plot(x,y, color = "c")
plt.xlabel(r'V$_{CE}$ [V]', loc='right')
plt.ylabel(r'I$_{C}$ [mA]', loc='top')
plt.title('Recta de Carga por Realimentacion (detallado)')
plt.grid(linestyle='--')
plt.ylim(ymin, ymin+1)
plt.xlim(xmin, xmin+2)
plt.legend(loc='best')
plt.savefig('PolRealimentacion(ZOOM).pdf')
