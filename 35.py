# create a function that returns both the area and circumference of a circle given its radius.
import math

def circle(r):
    area = ((22/7)*(r**2))
    circumference = 2*(22/7)*r
    return( area , circumference)
a , c = circle(3)

print("area:" ,int(a),"circumference:",int(c))