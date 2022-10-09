"""
x2 - 12x + 35 = 0
"""
import math
import numpy as np
from numpy.linalg import inv

a=1
b=-12
c=35

D=b**2-(4*a*c)
print(D)
if D>0:
    x_1=(-b+math.sqrt(D))/2*a
    x_2=(-b-math.sqrt(D))/2*a
    print(x_1,x_2)

"""
x=1,y=2,z=3

2x+3y+5z=23
1x+10y+2z=27
3x+y+5z=20
"""
a=[[2,3,5],
   [1,10,2],
   [3,1,5]]

a=inv(a)

b=[23,27,20]

s=np.dot(a,b)
print(s)