stored_value = 0


def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


def subtract(*args):
    difference = 0
    for number in args:
        difference -= number
    return difference


def multiply(*args):
    product = 0
    i = 0
    for number in args:
        if i == 0:
            product = number
        else:
            product = product * number
        i += 1
    return product


def divide(*args):
    quotient = 0
    i = 0
    for number in args:
        if i == 0:
            quotient = number
        else:
            quotient = quotient / number
        i += 1
    return quotient


def remainder(*args):
    remainder = 0
    i = 0
    for number in args:
        if i == 0:
            remainder = number
        else:
            remainder = remainder % number
        i += 1
    return remainder


print(
    "Welcome to the calculator. Please enter your numbers and the operation you would like to do."
)
while True:
    operation = input("What operation would you like to do? ")
    if operation == "add":
        numbers = int(input("How many numbers are you going to add? "))
        i = 0
        allNumbers = []
        while i < numbers:
            number = int(input("Put a number to add. "))
            allNumbers.append(number)
            i += 1
        added_sum = add(*allNumbers)
        stored_value += added_sum

    if operation == "subtract":
        numbers = int(input("How many numbers are you going to subtract? "))
        i = 0
        allNumbers = []
        while i < numbers:
            number = int(input("Put a number to subtract. "))
            allNumbers.append(number)
            i += 1
        subtracted_sum = subtract(*allNumbers)
        stored_value -= subtracted_sum
    if operation == "multiply":
        numbers = int(input("How many numbers are you going to multiply? "))
        i = 0
        allNumbers = []
        while i < numbers:
            number = int(input("Put a number to multiply. "))
            allNumbers.append(number)
            i += 1
        multiplied_sum = multiply(*allNumbers)
        stored_value *= multiplied_sum
    if operation == "divide":
        numbers = int(input("How many numbers are you going to divide? "))
        i = 0
        allNumbers = []
        while i < numbers:
            number = int(input("Put a number to divide. "))
            allNumbers.append(number)
            i += 1
        divided_sum = divide(*allNumbers)
        stored_value /= divided_sum
    if operation == "remainder":
        numbers = int(input("How many numbers are you going to subtract? "))
        i = 0
        allNumbers = []
        while i < numbers:
            number = int(input("Put a number to find the remainder of. "))
            allNumbers.append(*allNumbers)
            stored_value += remainder(*allNumbers)
    if operation == "calculate":
        print(stored_value)
        break
