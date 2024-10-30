#Integers to test
A, B, C = 1, 1, 3

print("A's value: " + str(A) + " ID: " + str(id(A))) #A and B have the same value, and thus the same ID.
print("B's value: " + str(B) + " ID: " + str(id(B)))
print("C's value: " + str(C) + " ID: " + str(id(C))) #C's ID will be different because it has a different value.

print()
#list to test
my_Array = [A, B, C]
print("Original list: ")
for x in my_Array:
    print(x, end=" ")
print("ID: " + str(id(my_Array)))

print()
#new list to test
my_Array.append(4)
print("New list: ")
for x in my_Array:
    print(x, end=" ")
print("ID: " + str(id(my_Array)))

"""
    Both lists above have the same ID
    despite the modification.
"""
print()
# variable modification test
B = 55
print("A's value: " + str(A) + " ID: " + str(id(A))) #if you modify b's value, its id changes.
print("B's value: " + str(B) + " ID: " + str(id(B)))

print()
new_Array = my_Array
print("my_Array ID: " + str(id(my_Array)) + "  Contains: " + str(my_Array)) #They share the same id
print("new_Array ID: " + str(id(my_Array)) + "  Contains: " + str(new_Array))

print()
new_Array.append(1001)
print("my_Array ID: " + str(id(my_Array)) + "  Contains: " + str(my_Array)) #modifying one array, modifies the other (they are the same entity/ shallow copy).
print("new_Array ID after modification: " + str(id(new_Array)) + "  Contains: " + str(new_Array))