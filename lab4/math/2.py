import math

def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = 5
base1 = 5
base2 = 6

area = trapezoid_area(height, base1, base2)
print("The area of the trapezoid is:", area)