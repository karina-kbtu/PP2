import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
print(calculate_sphere_volume())