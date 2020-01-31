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
    print(target)
    print(modSource)
    sourceTarget.append(target)
    sourceTarget.append(modSource)
    return sourceTarget

#Read Levenshtein Costs--------------------
srcTarget=[]
costsDictionary=processCosts("costs.csv")
costs2Dictionary=processCosts("costs2.csv")
srcTarget=processWords("words.txt")
print (srcTarget[1][4])


for x in range (2):
    print (x)










