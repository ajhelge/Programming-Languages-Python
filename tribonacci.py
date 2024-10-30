#Author: Alec Helgeson
#A program that recursivly calculates the first n numbers of the tribonacci sequence.
#which is an offshoot of the fibonacci sequence.
def tribonacci(n): #A funtion to compute the first n numbers of the tribonacci sequence.
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    
print("testing...") #A simple program to test the tribonacci funtion.

CONTROL = 20 #number of integers to print
print(f"First {CONTROL} numbers of tribonacci:", end="\n\n")
for i in range(CONTROL):
    print(tribonacci(i), end="  ")

print("\n\nEOP") #end of program