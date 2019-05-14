import matplotlib.pyplot as plt
from numpy import arange,sin,cos,tan
x=arange(0.0,6.2,0.2)
plt.plot(x,sin(x),'o-',cos(x),'*-')
plt.xlabel('x')
plt.ylabel('sinx  ,   cosx')
plt.grid(True)
plt.axis(ymin=0)
plt.axis(xmin=10)
plt.title('graph')
plt.legend(['sin','cosx'])
plt.show()
 
