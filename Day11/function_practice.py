import math

# Function 1 
def babble(stringOne, stringTwo):
    print(stringOne + stringTwo + stringTwo + stringOne)


# Function 2
def combiner(stringOne, stringTwo):
    print(stringOne[1:] + stringTwo[1:])

# Function 3

def shortener(word):
    if len(word) < 2:
        print("Error: Less than two character! Aborting...")
    else:
        print(word[0:2])

# Function 4

def emphasis(word):
    print(word.upper() + "!!!")

# Function 5

def combo(stringOne, stringTwo):
    if len(stringOne) > len(stringTwo):
        print(stringTwo + stringOne + stringTwo)
    elif len(stringOne) < len(stringTwo):
        print(stringOne + stringTwo + stringOne)
    else:
        print(stringOne + stringTwo + stringOne)

# Function 6

def sss_solver(side1: float, side2: float, side3: float): # typed function
    a = side1
    b = side2
    c = side3

    big_a = radians_to_degrees(math.acos(((a * a) - (b * b) - (c * c)) / (-2 * b * c)))
    big_b  = radians_to_degrees(math.acos(((b * b) - (a * a) - (c * c)) / (-2 * a * c)))
    big_c = radians_to_degrees(math.acos(((c * c) - (b * b) - (a * a)) / (-2 * a * b)))
    if (round(big_a + big_b + big_c)) != 180:
        print("Error: Not a triangle! Aborting...")
        exit()
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Solved! \nThe angle of A is " + str(round(big_a, 3)) + " degrees. \nThe angle of B is " + str(round(big_b, 3)) + " degrees. \nThe angle of C is " + str(round(big_c, 3)) + " degrees. \nThe area of the triangle is " + str(round(area, 3)) + " units squared.")

# Function 7 
def radians_to_degrees(radians):
    return (radians * 180 / math.pi)

sss_solver(7, 12, 18)
