import csv

file = open("ExampleData.csv")
dataReader = csv.reader(file)
numList = []
for [num, value] in dataReader:
    numList.append(num)

print(numList)
