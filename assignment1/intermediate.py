import math
def calculate_area(shape, *args):
    if shape == "rectangle":
        return args[0] * args[1]
    elif shape == "square":
        return args[0] ** 2
    elif shape == "circle":
        return math.pi * args[0] ** 2

print(calculate_area("rectangle",5,10))