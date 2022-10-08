"""
x2 - 12x + 35 = 0
"""
import math

a=1
b=-12
c=35

D=b**2-(4*a*c)
print(D)
if D>0:
    x_1=(-b+math.sqrt(D))/2*a
    x_2=(-b-math.sqrt(D))/2*a
    print(x_1,x_2)