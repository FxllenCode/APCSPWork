import csv

# Use the data reader to open the file and put it all in one data list
file = open("HalloweenBoxOfficeUK.csv")
opened = csv.reader(file)
rows = []
for row in opened:
    rows.append(row)
nameList = []
originList = []
grossList = []
distList = []
weeksList = []
cinemasList = []

for row in rows:
    nameList.append(row[0])
    originList.append(row[1])
    grossList.append(int(row[2]))
    distList.append(row[3])
    weeksList.append(int(row[4]))
    cinemasList.append(int(row[5]))


print("Find the largest amount grossed.")

print(max(grossList))

print("Find the smallest amount grossed.")

print(min(grossList))


print("Find the amount of movies that were at least partially made in the U.S.")

count = 0

for country in originList:
    if country.find("US"):
        count += 1
print(count)

print('Find the amount of movies that start with the letter "S".')
count = 0
for name in nameList:
    if name.find("S") == 0:
        count += 1
print(count)

print("Find the average amount of theaters that the movies were in.")

print(sum(cinemasList) / len(cinemasList))

print("Name of highest grossing movie.")
print(nameList[grossList.index(max(grossList))])

print("Name of movie with the most weeks in theaters.")
print(nameList[weeksList.index(max(weeksList))])

print("Movies out for a week or less.")

for i in range(len(weeksList)):
    if int(weeksList[i]) <= 1:
        print(nameList[i])
