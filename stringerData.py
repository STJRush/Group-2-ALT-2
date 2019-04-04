import re

datalisted = [['#student', 'sCore.'], ['Mr. Joer', '2 points'], ['Lad John', 'six'], ['Mr. Jimmy', '2%']]
print (datalisted)

stringerData=str(datalisted)

stringerData = re.sub('[.!%#rMLad ]','', stringerData)
stringerData = re.sub('six', '6', stringerData)
stringerData = re.sub('sCoe', 'Score', stringerData)
stringerData = re.sub('stuent', 'Student', stringerData)
stringerData = re.sub('points', '', stringerData)

print("Here is the cleaned up list that will be written to the new csv and/or be graphed")
print (stringerData)