from scipy import linspace, pi, sin
from pylab import plot, legend, show, title
from pylab import xlabel, ylabel

x = linspace(-2*pi,2*pi,100)
plot(x,sin(x))
legend(['sin(x)'])
title('Sine plot')
xlabel('x')
ylabel('sin(x)')
show()
