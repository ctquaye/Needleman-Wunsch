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
srcTarget=processWords("words.txt")
#print (srcTarget[1])

#Retrieve Sequence 1 and Sequence 2
for tgt in range(len(srcTarget)):
    Sequence1 = srcTarget[0][tgt]
    for src in range(len(srcTarget)):
       Sequence2 = srcTarget[1][src]
Sequence2= srcTarget[0][0]
Sequence1=srcTarget[1][0][0]

Sequence2='mischevious'
Sequence1='mischief'

print(Sequence1," ",Sequence2)

#INITIALIZATION STEP -------------------------------------------------------------

for rowSeq1 in range (len(Sequence1)+1):
    new=[]; new2=[]
    for colSeq2 in range (len(Sequence2)+1):
        if(rowSeq1 ==0) :
            new.append(colSeq2)
            new2.append(1000000)
        elif(colSeq2==0):
            new.append(rowSeq1)
            new2.append(1000000)
        else:
            new.append(0)
            new2.append("x")
    Matrix.append(new)
    path.append(new2)

#SCORING --------------------------------------------------------------------------
for rowSeq1 in range (len(Sequence1)):
    for colSeq2 in range (len(Sequence2)):
        row = rowSeq1+1; col = colSeq2 +1   #skip row 0 and col 0

        #check if match/mismatch
        if(Sequence1[rowSeq1] == Sequence2[colSeq2]):
            match_mismatch = match
        else:
            findCostKey = Sequence1[rowSeq1]+Sequence2[colSeq2]
            if findCostKey in costs2Dictionary:
                mismatch=costs2Dictionary.get(findCostKey)
                #print(mismatch)
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

for rowSeq1 in range(len(Sequence1)+1):
   for colSeq2 in range(len(Sequence2)+1):
      print(path[rowSeq1][colSeq2],end=" ")
   print()

print("length: ",len(path[1][1]))

x=-1; y=-1; resuSeq1=[]; resuSeq2=[]; trace=path[y][x][0]; z=0;  operationString=[]
while(trace != 1000000 or y!= -(len(Sequence1)+1) or x != -(len(Sequence2)+1)):
#substitution
    if(trace==0):
        resuSeq2.append(Sequence2[x])
        resuSeq1.append(Sequence1[y])
        if(Sequence1[y]== Sequence2[x]):
            operationString.append("k")
        else:
            operationString.append("s")
        y=y-1; x=x-1
        if (y == -(len(Sequence1)+1)):
            trace=path[y][x]
        else:
            numOfPaths = len((path[y][x]))
            numOfPaths=numOfPaths-1
            z = random.randint(0, numOfPaths)
            trace=path[y][x][z]
#deletion
    elif(trace==1):
        resuSeq2.append(Sequence2[x])
        resuSeq1.append("*")
        operationString.append("d")
        x=x-1
        if (x == -(len(Sequence2)+1)):
            trace=path[y][x]
        else:
            numOfPaths = len((path[y][x]))
            numOfPaths = numOfPaths - 1
            z = random.randint(0, numOfPaths)
            trace = path[y][x][z]
#insertion
    elif(trace==2):
        resuSeq2.append("*")
        resuSeq1.append(Sequence1[y])
        operationString.append("i")
        y=y-1
        if (y == -(len(Sequence1)+1)):
            trace=path[y][x]
        else:
            numOfPaths = len((path[y][x]))
            numOfPaths = numOfPaths - 1
            z = random.randint(0, numOfPaths)
            trace = path[y][x][z]

    elif (x == -(len(Sequence2) + 1)):
        resuSeq2.append("*")
        resuSeq1.append(Sequence1[y])
        operationString.append("i")
        y = y - 1
        trace = path[y][x]

    elif (y == -(len(Sequence1) + 1)):
        resuSeq1.append("*")
        resuSeq2.append(Sequence2[x])
        operationString.append("d")
        x = x - 1
        trace = path[y][x]

for j in reversed(resuSeq1):
    print(j, end="")
print()
for q in range(len(resuSeq1)):
    print("|", end="")
print()
for i in reversed(resuSeq2):
    print(i, end="")
print()
for k in reversed(operationString):
    print(k, end="")
print()

