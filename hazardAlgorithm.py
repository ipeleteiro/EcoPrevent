# This algorithm is quite simple, 
# but it uses the '30 rule' for assesing fires as well as considering fuel and health 

# If we had more time, an AI could be developed to improve this 
# assesment system based on wildfire data

temp = float(input("Enter the current temperature (C): "))
humidity = int(input("Enter the current humidity (%): "))
speed = float(input("Enter the current wind speed (m/s): "))
tree = input("Enter the main tree type (lowercase and avoid specific names, eg: 'pine' not 'scots pine'): ")
health = int(input("Enter the health (%): "))

hazard = 0

if temp > 30:
    hazard += 1
if humidity < 30:
    hazard += 1
if speed > 30:
    hazard += 1

tree_dictionary = {'ash':3, 'pine':1, 'spruce':1, 'oak': 3, 'larch':1, 'hornbeam':2, 'fir':1,'beech':2,'maple':2}
#Tree grading from South Yorkshire firewood

if tree in tree_dictionary:
    hazard += tree_dictionary[tree]
else:
    print("That tree is not in our database, please try again.")

if health < 50:
    hazard += 1


print("The area's hazard level is:", hazard)
