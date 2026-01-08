car1 = {}

car1['brand'] = input("Brand 1: ")
car1['model'] = input("Model 1: ")
car1['horse_power'] = input("Horse powers of car1: ")

car2 = {}

car2['brand'] = input("Brand 2: ")
car2['model'] = input("Model 2: ")
car2['horse_power'] = input("Horse powers of car2: ")

if car1['horse_power'] > car2['horse_power']:
    print(f"{car1['brand']} {car1['model']} is faster")

elif car2['horse_power'] > car1['horse_power']:
    print(f"{car2['brand']} {car2['model']} is faster")

else:
    print("The two cars are equal")
