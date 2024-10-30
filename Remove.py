guess_list = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
availble_for_guessing = 'abcdefghijklmnopqrstuvwxyz'

inputString = input("What letters do you guess? ")#GATHER INPUT

for char in inputString:
    guess_list.append(char)#append the letter to the list of guessed letters.
    if char in list(availble_for_guessing):#convert available_for_guessing to a list.
        availble_for_guessing = (availble_for_guessing.replace(char, "")) #if the letter guessed is in the availible list, remove it.

print(guess_list)
print(alphabet)
print(availble_for_guessing)