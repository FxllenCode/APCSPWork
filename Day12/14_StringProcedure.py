import math

def sss_solver(side1: float, side2: float, side3: float): # typed function
    a = side1
    b = side2
    c = side3
    # Use the law of cosines to find the angle lengths for the respecting Length
    big_a = radians_to_degrees(math.acos(((a * a) - (b * b) - (c * c)) / (-2 * b * c))) 
    big_b  = radians_to_degrees(math.acos(((b * b) - (a * a) - (c * c)) / (-2 * a * c)))
    big_c = radians_to_degrees(math.acos(((c * c) - (b * b) - (a * a)) / (-2 * a * b)))
    if (round(big_a + big_b + big_c)) != 180: # This should *never* happen, but if it does, panic panic panic!
        print("Error: Not a triangle! Aborting...")
        exit()
    s = (a + b + c) / 2 #
    area = math.sqrt(s * (s - a) * (s - b) * (s - c)) # Heron's formula
    print("Solved! \nThe angle of A is " + str(round(big_a, 3)) + " degrees. \nThe angle of B is " + str(round(big_b, 3)) + " degrees. \nThe angle of C is " + str(round(big_c, 3)) + " degrees. \nThe area of the triangle is " + str(round(area, 3)) + " units squared.")

def radians_to_degrees(radians):
    return (radians * 180 / math.pi)

sss_solver(7, 12, 18)
