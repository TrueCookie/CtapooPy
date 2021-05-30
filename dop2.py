import random
from sympy import *

#a = random.randint(5, 10)
#w = random.randint(5, 10)
a = 5
w = 3.14/2


t = Symbol('t')

x = a * cos(w * t)
x_prime = x.diff(t)
x_prime2 = x_prime.diff(t)

# task #1
p = plot( x, x_prime, x_prime2, (t, 0, 3.14), show=false)
p[0].line_color = 'red'
p[1].line_color = 'green'
p[2].line_color = 'blue'
p.show()

# task #2
#x_sym = Symbol('a * cos(w * t)')
#p2 = plot(x_prime, x_prime2, (t, 0, 20), show=false)
#p2[0].line_color = 'red'
#p2[1].line_color = 'green'
#p2.show()
