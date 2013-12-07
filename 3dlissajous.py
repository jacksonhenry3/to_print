from mayavi.mlab import *
from numpy import *
x = linspace(0,2*pi,5000)

def makeFig(a,b,c):
    plot3d(cos(a*x),sin(b*x),sin(c*x),tube_sides=100)
    savefig('Documents/GitHub/printer_files/lissajous/Lissajous'+str(a)+str(b)+str(c)+'.obj')
    show()
    
makeFig(2,15,12)