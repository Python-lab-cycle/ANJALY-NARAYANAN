import math
def circlearea(r):
    area=math.pi*r**2
    return area
def circleperimeter(r):
    perimeter=2*math.pi*r
    return perimeter
def spherearea(r):
    area=4*math.pi*r**2
    return area
def sphereperimeter(r):
    perimeter=(4/3)*math.pi*r**3
    return perimeter
def cuboidarea(l,w,h):
    area=(2*l*w)+(2*l*h)+(2*h*w)
    return area
def cuboidperimeter(l,w,h):
    perimeter=4*(l+w+h)
    return perimeter
