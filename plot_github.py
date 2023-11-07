import numpy as np
import pylab

x=np.linspace(-1,1,100)
y=(x)*np.sin(1/x)
pylab.plot(x, y,'*r')
pylab.xlabel('x')
pylab.ylabel('y')