# za list
myList = ['apple', 'watermelon', 'banana', 'apple']

has_duplicates = False

for item in myList:
    if myList.count(item) > 1:
        has_duplicates = True
        break

if has_duplicates:
    print("There are equal items in the list")

else:
    print("All items are unique")

# za tuple
myTuple = ('apple', 'watermelon', 'banana', 'apple')

has_duplicate = False

for item in myTuple:
    if myTuple.count(item) > 1:
        has_duplicate = True
        break

if has_duplicate:
    print("There are equal items in the tuple")

else:
    print("All items are unique")
