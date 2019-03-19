import statistics
numbers=[1,2,3,4,5,5]

def minmax(numbers):
    min_val = min(numbers)
    max_val = max(numbers)

    return (max_val-min_val)

print("the range is:")
print(minmax(numbers))

print("the mode is:")
print(statistics.mode(numbers))
