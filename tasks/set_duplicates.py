mySet = {'peach', 'chips', 'pizza', 'orange', 'apple', 'banana', 'cherry'}
myList = ["apple", "pizza"]

mySet.difference_update(set(myList))

print(mySet)
