import statistics
numbers=[1,2,3,4,5,5]


#def getrange(numbers):
    #return max(numbers)-min(numbers)

#print(getrange)

def minmax(numbers):
    min_val = min(numbers)
    max_val = max(numbers)

    return (max_val-min_val)

print(minmax(numbers))
print(statistics.mode(numbers))