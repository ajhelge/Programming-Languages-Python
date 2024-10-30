inputString = input("Please input a string: ")#GATHER INPUT

lettercount = {} #initialize dictionary, key value pairs, whoa!

inputString = inputString.lower() #convert inputstring to the lower case version i.e. A --> a

for char in inputString:    #for all charecters in input string, 1: check if the are a alphabetical charecter, 2: put it in the letter count dictoinary.
    if char.isalpha():
        if char in lettercount:
            lettercount[char] += 1
        else:
            lettercount[char] = 1

for letter in sorted(lettercount): #for all the letters in the lettercount dictoinary, print the letter and its total count (letter:count)
    print(f"{letter} : {lettercount[letter]}") #format string and print