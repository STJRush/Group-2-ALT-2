import csv
import re

def clean_stuff(valu):
    valu=re.sub('[.!@#$&*^<]','', valu)
   
    
    return valu

f = open("ALT 2 project.csv", newline = '')
reader = csv.reader(f)

#header = next(reader)

dataListed= [row for row in reader]

row_count = sum(1 for row in dataListed)
print("number of rows is", row_count)

print("Here is the orginal list in the file...")
print(dataListed, "\n\n")

print("Here is the cleaned up list that will be written to the new csv and/or graphed")

xValuesList=[]


for i in range(row_count):
    valu = dataListed[i][1]
    cleanxVal=clean_stuff(valu)
    xValuesList.append(cleanxVal)
    
yValuesList=[]

for i in range(row_count):
    valu = dataListed[i][2]
    cleanyVal=clean_stuff(valu)
    yValuesList.append(cleanyVal)


print(xValuesList)
print(yValuesList)