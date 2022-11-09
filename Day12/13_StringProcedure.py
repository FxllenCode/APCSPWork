def split(word):
    length = int(len(word)/2)
    if (len(word) < 2) or (len(word)%2!=0):
        print("Error: Less than two or odd number of characters in string")
    else:
        print((word[:length])+"-"+(word[length:]))
split(input("What word do you want to split? "))