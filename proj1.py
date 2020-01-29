#!/usr/bin/env python3.7
import sys
import re


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
    print(costDictionary)
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
#Read costs.csv

match = 0
mismatch = -1
gapPenalty = 1
match_mismatch = 0

#Read Levenshtein Costs--------------------
srcTarget=[]
costsDictionary=processCosts("costs.csv")
costs2Dictionary=processCosts("costs2.csv")
srcTarget=processWords("words.txt")
#print (srcTarget[1])

#Retrieve Sequence 1 and Sequence 2
#for tgt in range(len(srcTarget)):
 #   Sequence1 = srcTarget[0][tgt]
  #  for src in range(len(srcTarget)):
   #     Sequence2 = srcTarget[1][src]
Sequence1= srcTarget[0][0]
Sequence2=srcTarget[1][0][0]

Sequence1='execution'
Sequence2='intention'

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
            if findCostKey in costsDictionary:
                mismatch=costsDictionary.get(findCostKey)
                #print(mismatch)
            match_mismatch = mismatch

        diagonal = Matrix[row-1][col-1]
        left = Matrix[row][col-1]
        top = Matrix[row-1][col]

        substitute = diagonal +  int(match_mismatch)
        delete = left + gapPenalty
        insert = top + gapPenalty
        #print(delete,insert, substitute)
        findMin = [substitute, delete, insert]
        min_value = min(findMin)
        hop = findMin.index(min(findMin))
        Matrix[row][col]=min_value
        path[row][col]=hop

for rowSeq1 in range(len(Sequence1)+1):
   for colSeq2 in range(len(Sequence2)+1):
      print(Matrix[rowSeq1][colSeq2],end=" ")
   print()

x=-1; y=-1; resuSeq1=[]; resuSeq2=[]; trace=path[y][x];
while(trace != 1000000 or y!= -(len(Sequence1)+1) or x!= -(len(Sequence2)+1)):
    if(trace==0):
        resuSeq2.append(Sequence2[x])
        resuSeq1.append(Sequence1[y])
        y=y-1; x=x-1
        trace=path[y][x]

    elif(trace==1):
        resuSeq2.append(Sequence2[x])
        resuSeq1.append("*")
        x=x-1
        trace=path[y][x]

    elif(trace==2):
        resuSeq2.append("*")
        resuSeq1.append(Sequence1[y])
        y=y-1
        trace=path[y][x]

    elif (y == -(len(Sequence1) + 1)):
        resuSeq2.append(Sequence2[x])
        resuSeq1.append("*")
        x = x - 1
        trace = path[y][x]

    elif (y == -(len(Sequence1) + 1)):
        resuSeq1.append(Sequence1[y])
        resuSeq2.append("*")
        y = y - 1
        trace = path[y][x]

for i in reversed(resuSeq2):
    print(i, end="")
print()

for j in reversed(resuSeq1):
    print(j, end="")
print("\n")