from matplotlib import pyplot as plt
import numpy as np
class Point:
    
    def __init__(self, x1, y1, col, label):
        self.x = [x1]
        self.y = [y1]
        self.col = col
        self.lab = label

#3 Pol por div de tension
icMax = 2.79
vMax = 12
y = [icMax, 0]
x = [0, vMax]
listop=[]
pt = Point(3.31, 2.02, 'c', r'$\beta_{prom} = 377$')
listop.append(Point(3.13,2.06,"r", r'$\beta = 416$' ))
listop.append(Point(3.20,2.05, "b", r'$\beta = 360$'))
listop.append(Point(3.17,2.06, "g", r'$\beta = 356$'))
listop.append(Point(3.19,2.06, "m", r'$\beta = 367$'))
listop.append(Point(3.19,2.08, "y", r'$\beta = 386$'))
plt.plot(pt.x, pt.y, marker = "o", color = pt.col, markersize = 10.0)
for poi in listop:
    plt.plot(poi.x, poi.y, marker = "o", color = poi.col)
plt.plot(x,y, color = "c")
plt.xlabel(r'V$_{CE}$ [V]', loc='right')
plt.ylabel(r'I$_{C}$ [mA]', loc='top')
plt.title('Recta de Carga por Divisor de Tensión')
plt.grid(linestyle='--')
plt.ylim(0, 3)
plt.xlim(0, 13)
plt.savefig('PolDivDeTension.pdf')
#2 Pol por div de tension ZOOM
ymin = 1.55
xmin = 2.25
plt.plot(pt.x, pt.y, marker = "o", color = pt.col, markersize = 10.0, label = pt.lab)
for poi in listop:
    plt.plot(poi.x, poi.y, marker = "o", color = poi.col, label = poi.lab)
plt.plot(x,y, color = "c")
plt.xlabel(r'V$_{CE}$ [V]', loc='right')
plt.ylabel(r'I$_{C}$ [mA]', loc='top')
plt.title('Recta de Carga por Divisor de Tensión (detallado)')
plt.grid(linestyle='--')
plt.ylim(ymin, ymin+1)
plt.xlim(xmin, xmin+2)
plt.legend(loc='best')
plt.savefig('PolDivDeTension(ZOOM).pdf')
