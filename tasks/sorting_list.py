myList = []

n = int(input("n = "))

for i in range(n):
    myList.append(int(input(f"Element {i+1}: ")))

print(myList)

myList.sort()

print(myList)
