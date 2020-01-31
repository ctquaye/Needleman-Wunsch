#Determine possible paths---------------------------------------
import random
findMin=[3,4,1,1]
possiblePaths=[]
minValue=min(findMin)
for m in range(len(findMin)):
    if (findMin[m]==minValue):
        possiblePaths.append(m)
print (possiblePaths)

for row in range(len(findMin)):
    findMin[row]=possiblePaths

print(findMin)
x=random.randint(0,)
print(x)

for nextCost in range(2):
    if (nextCost) == 1:
        Dictionary = costsDictionary
    else:
        Dictionary = costs2Dictionary