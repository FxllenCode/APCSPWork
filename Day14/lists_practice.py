import math

def single_element_list(list):
    single_element_list = []
    for i in list:
        if list.count(i) == 1:
            single_element_list.append(i)
    return single_element_list

def swap_min_max(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i < min:
            min = i
        if i > max:
            max = i
    min_index = list.index(min)
    max_index = list.index(max)
    list[min_index], list[max_index] = list[max_index], list[min_index]
    return list


def compare_averages(list1, list2): # Returns True if list1 has a higher average than list2
    sum1 = 0
    sum2 = 0
    for i in list1:
        sum1 += i
    for i in list2:
        sum2 += i
    average1 = sum1 / len(list1)
    average2 = sum2 / len(list2)
    if average1 > average2:
        return True
    else:
        return False

def grocery_list():
    grocery_list = []
    while True:
        item = input("Enter an item you need from the store: ")
        answer = input("Do you need to refrigerate this item? (y/n) ")
        if answer == "y":
            grocery_list.append(item)
        answer = input("Do you need to add another item? (y/n) ")
        if answer == "n":
            break
    return grocery_list


def same_sign(list: list):
    new_list = []
    for number in list:
        if (list.count(abs(number)) > 1) and (list.count(number) == 1):
            new_list.append(number)
    return new_list

print(same_sign([1, -1]))


def even_odd_count(list):
    even_count = 0
    odd_count = 0
    for number in list:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


def long_names(list):
    long_names = []
    for name in list:
        if len(name) >= 5:
            long_names.append(name)
    if len(long_names) == 0:
        print("Everyone has a short name!")
    else:
        print(long_names)