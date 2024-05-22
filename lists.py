#Exerecise 1
numList= [1,2,3,4,5,6,7]

print(max(numList))

#Exercise 2
char= ['a','b','c','d']
revChar=[]

for x in char:
   revInd=char.index(x) + 1
   character= char[-revInd]
   revChar.append(character)

print(revChar)

#Exercise 3
groceries=["bread","milk","eggs"]
groceries.insert(4,"spice")

print(groceries)

groceries.remove("bread")

print(groceries)

groceries.append('drinking chocolate')

print(groceries)
