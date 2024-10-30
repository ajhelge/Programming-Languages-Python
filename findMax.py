# A recursive way to find the max value in a list of values.

def findMax(list):
    if (len(list) <= 1): #base case
        return list[0]
    else: 
        max = findMax(list[1:]) # Slice off list[0] and recurse
    return max if max > list[0] else list [0] # return the bigger value

a = [1, 2, 3, 21, 5, 6, 20]

b = findMax(a)

print(b)