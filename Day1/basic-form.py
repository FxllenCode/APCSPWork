class Information: 
    def __init__(self, name, age, grade, address): 
        self.name = name
        self.age = age
        self.grade = grade
        self.address = address


info = Information(input("What is your name? "), int(input("What is your age? ")), int(input("What is your grade? ")), input("What is your address? "))


print("Hello there " + info.name + "!")
print("You are " + str(info.age) + " years old.")
print("You are in grade " + str(info.grade) + ".")
print("You live at " + info.address + ".")