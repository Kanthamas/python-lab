# Exercise 1: Introducing the list data type (Mutable)
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# get "apple"
print(myFruitList[0])

# modify item in a list
myFruitList[2] = "orange"

# get each item
for fruit in myFruitList:
    print(fruit)

# Exercise 2: Introducing the tuple data type (Immutable)
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# get "apple"
print(myFinalAnswerTuple[0])

for fruit in myFinalAnswerTuple:
    print(fruit)

# Exercise 3: Introducing the dictionary data type (Mutable)
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# get "apple"
print(myFavoriteFruitDictionary["Akua"])

myFavoriteFruitDictionary["Paulo"] = "coconut"

for fruit in myFavoriteFruitDictionary:
    print(myFavoriteFruitDictionary[fruit])