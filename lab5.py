# Exercise 1: Creating a mixed-type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

# display indices in the list 
for i in range(len(myMixedTypeList)): 
    print(i) 

for i in enumerate(myMixedTypeList): 
    print(i) 


