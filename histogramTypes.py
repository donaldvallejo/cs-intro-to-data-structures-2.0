listOfListsHistogram = [["bird", 3],["cat", 5],["dog", 5]]
print(listOfListsHistogram)

innerList = listOfListsHistogram[2]
print(innerList[0])

# UPDATE AN ITEAM
listOfListsHistogram[0][1] = 6
print(listOfListsHistogram)

#TODO: write a loop that prints out the animal word and the count in list_of_lists_histogram
#update the count for "cat" by adding 1

for i in listOfListsHistogram:
    animal = i[0]
    count = i[1]
    print(f"the animal is {animal} and the count is {count}")

# You can also write it this way 
for i in range(len(listOfListsHistogram))
animal = listOfListsHistogram[i][0]
count = listOfListsHistogram[i][1]
print(listOfListsHistogram[i])

# update cat
listOfListsHistogram[1][1] += 1
print(f" after adding one to cat {listOfListsHistogram[1][1]}")


dictionary_histogram = {"cupcake": 33, "donut":4, "cake":50}

#TODO: write a loop that prints out the food word and the count in dictionary_histogram
#update the count for "cupcake" by adding 1
for k,v in dictionary_histogram.items():
    print(f"the dessert is {k} and the count is {v}")

# update by 1
dictionary_histogram["cupcake"] += 1
print(f" after adding one to cupcake {dictionary_histogram}")



listOfTuplesHistogram = [("snowboarding", 4), ("basketball", 8), ("football", 9)]
#update the count for "football" by adding 1

# print(listOfTuplesHistogram[0][1])
print("test " + listOfTuplesHistogram[2][1])


listOfTuplesHistogram[2][1] += 1 
listOfTuplesHistogram[2][1] = ("football", 10)
# update number value
listOfTuplesHistogram[2] = (listOfTuplesHistogram[2][0], listOfTuplesHistogram[2][1] + 1)
# update string key
listOfTuplesHistogram[2] = (listOfTuplesHistogram[2][0] + "new string")


print("tried to change" + listOfTuplesHistogram[2][1])

# implement and add to your histogram file 
# list_histogram
# tuple_histogram
# stretch: count_histogram()
 