import math

def area_of_regular_polygon(n, s):
    return (n * s**2 / (4 *math.tan(math.pi / n)))
n=4
s=25
area=area_of_regular_polygon(n, s)
print(area)
