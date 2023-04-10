import random

num = ""
for i in range((255 * 255 * 255)): 
    num += str(random.randint(0, 1))

open("h.txt", "w").write(num)