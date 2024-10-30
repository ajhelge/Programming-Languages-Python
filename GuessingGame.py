input1 = input("Word to guess: ")#GATHER INPUT

input2 = input("Letters you guess: ")

#funtion to test
def isGuessed(word, list_of_guesses):
    
    word = set(word) #convert word and list_of_guesses to sets

    list_of_guesses = set(list_of_guesses)

    if(word.issubset(list_of_guesses)): #checks if all letters in guesses are in the secret word.
        return True
    return False

print(isGuessed(input1, input2)) #test the function.

