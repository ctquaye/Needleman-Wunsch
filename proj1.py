#!/usr/bin/env python3.7
import sys
import re
import random

def processCosts(str):
    totalLines=[]
    with open(str, "r") as costFile:
        line = [re.split('[\n|,]', l) for l in costFile]
        totalLines.append(line)
    lineArray = totalLines[0]

    print(len(lineArray))
    costDictionary={}
    for row in range(len(lineArray)):
        for col in range(len(lineArray[row])):
            if ((row and col) != 0):
                costDictionary.update({lineArray[row][0] + lineArray[0][col]: lineArray[row][col]})
                # print(lineArray[row][col], end='')
        # print()
    #print(costDictionary)
    return costDictionary

def processWords(str):
    target=[]
    sourceTarget=[]
    temp=[]
    modSource=[]
    with open(str, "r") as costFile:
        line = [l.split() for l in costFile]
    for row in range(len(line)):
        for col in range(len(line[row])):
            if(col==0):
                target.append(line[row][col])
    source=line[0:]
    for src in range(len(source)):
        source[src].pop(0)
        temp.append(source)
        modSource=temp[0]
 #   print(target)
  #  print(modSource)
    sourceTarget.append(target)
    sourceTarget.append(modSource)
    return sourceTarget

def findCost(costFile, srcWord,tgtWord, row, col,cost):
    findCostKey = srcWord[row] + tgtWord[col]
    if findCostKey in costFile:
        cost = costFile.get(findCostKey)
    return (cost)

Matrix =[]
path =[]

#READ COSTS----------------------------------------------------------------------
#initialize variables
match = 0
gapPenalty = 1
match_mismatch = 0
srcTarget=[]
#Read Levenshtein Costs--------------------
costsDictionary=processCosts("costs.csv")
#Read Confusionn Matrix--------------------
costs2Dictionary=processCosts("costs2.csv")
#Read Target word and Source words
srcTarget=processWords("words.txt")

#Retrieve Target and Source
for tgt in range(len(srcTarget)):
    sourceWord = srcTarget[0][tgt]
    for src in range(len(srcTarget)):
       targetWord = srcTarget[1][src]
targetWord= srcTarget[0][0]
sourceWord=srcTarget[1][0][0]

<<<<<<< HEAD
Sequence2='mischevious'
Sequence1='mischief'
=======
targetWord='mischevious'
sourceWord='mischief'
>>>>>>> 932fe489fa303f8f45ae52bc9938698d7defbe1d

print(sourceWord," ",targetWord)

#INITIALIZATION STEP -------------------------------------------------------------
for rowSrc in range (len(sourceWord)+1):
    new=[]; new2=[]
    for colTgt in range (len(targetWord)+1):
        if(rowSrc ==0) :
            new.append(colTgt)
            new2.append(8888)
        elif(colTgt==0):
            new.append(rowSrc)
            new2.append(8888)
        else:
            new.append(0)
            new2.append("x")
    Matrix.append(new)
    path.append(new2)

#SCORING --------------------------------------------------------------------------

for rowSrc in range (len(sourceWord)):
    for colTgt in range (len(targetWord)):
        row = rowSrc+1; col = colTgt +1   #skip row 0 and col 0
        cost = 0
        #check if match/mismatch
        if(sourceWord[rowSrc] == targetWord[colTgt]):
            match_mismatch = match
        else:
<<<<<<< HEAD
            findCostKey = Sequence1[rowSeq1]+Sequence2[colSeq2]
            if findCostKey in costs2Dictionary:
                mismatch=costs2Dictionary.get(findCostKey)
                #print(mismatch)
=======
            mismatch=findCost(costsDictionary,sourceWord,targetWord,rowSrc,colTgt,cost)
>>>>>>> 932fe489fa303f8f45ae52bc9938698d7defbe1d
            match_mismatch = int(mismatch)

        diagonal = Matrix[row-1][col-1]
        left = Matrix[row][col-1]
        top = Matrix[row-1][col]

        substitute = diagonal +  int(match_mismatch)
        delete = left + gapPenalty
        insert = top + gapPenalty
        #print(delete,insert, substitute)
        # Determine possible paths---------------------------------------
        findMin = [substitute, delete, insert]
        possiblePaths = []
        minValue = min(findMin)
        for m in range(len(findMin)):
            if (findMin[m] == minValue):
                possiblePaths.append(m)
        #print(possiblePaths)

        Matrix[row][col]=minValue
        path[row][col]=possiblePaths

for rowSrc in range(len(sourceWord)+1):
   for colTgt in range(len(targetWord)+1):
      print(path[rowSrc][colTgt],end=" ")
   print()

print("length: ",len(path[1][1]))

x=-1; y=-1; resuSrc=[]; resuTgt=[]; trace=path[y][x][0]; z=0;  operationString=[]
while(trace != 8888 or y!= -(len(sourceWord)+1) or x != -(len(targetWord)+1)):
#substitution
    if(trace==0):
        resuTgt.append(targetWord[x])
        resuSrc.append(sourceWord[y])
        if(sourceWord[y]== targetWord[x]):
            operationString.append("k")
        else:
            operationString.append("s")
        y=y-1; x=x-1
        if ((y == -(len(sourceWord)+1)) or (x == -(len(targetWord)+1))):
            trace=path[y][x]
        else:
            numOfPaths = len((path[y][x]))
            numOfPaths=numOfPaths-1
            z = random.randint(0, numOfPaths)
            trace=path[y][x][z]

#deletion
    elif(trace==2):
        resuTgt.append("*")
        resuSrc.append(sourceWord[y])
        operationString.append("d")
        y=y-1
        if (y == -(len(sourceWord)+1)):
            trace=path[y][x]
        else:
            numOfPaths = len((path[y][x]))
            numOfPaths = numOfPaths - 1
            z = random.randint(0, numOfPaths)
            trace = path[y][x][z]

#insertion
    elif(trace==1):
        resuTgt.append(targetWord[x])
        resuSrc.append("*")
        operationString.append("i")
        x=x-1
        if (x == -(len(targetWord)+1)):
            trace=path[y][x]
        else:
            numOfPaths = len((path[y][x]))
            numOfPaths = numOfPaths - 1
            z = random.randint(0, numOfPaths)
            trace = path[y][x][z]

    elif (x == -(len(targetWord) + 1)):
        resuTgt.append("*")
        resuSrc.append(sourceWord[y])
        operationString.append("d")
        y = y - 1
        trace = path[y][x]

    elif (y == -(len(sourceWord) + 1)):
        resuSrc.append("*")
        resuTgt.append(targetWord[x])
        operationString.append("i")
        x = x - 1
        trace = path[y][x]

#Calculate cost---------------------------------
editDistance=0
for c in range(len(operationString)):
    cost = 0
    if((operationString[c]=='i') or (operationString=='d')):
        editDistance = editDistance + 1
    elif(operationString[c]=='k'):
        pass
    else:
       subCost = findCost(costsDictionary,resuSrc,resuTgt,c,c,cost)
       editDistance = editDistance + int(subCost)

#Display output---------------------------------
for j in reversed(resuSrc):
    print(j, end="")
print()
for q in range(len(resuSrc)):
    print("|", end="")
print()
for i in reversed(resuTgt):
    print(i, end="")
print()
for k in reversed(operationString):
    print(k, end="")
print(" (",editDistance,")")

