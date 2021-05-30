import random
from sympy import *

x = Symbol('x')

y = cos(x)
y_prime = y.diff(x)
y_prime2 = y.diff(x, 2)
p = plot(y, y_prime, y_prime2, (x, 0, 20), show=false)

p[0].line_color = 'red'
p[1].line_color = 'green'
p[2].line_color = 'blue'
p.show()