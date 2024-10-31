from int_Set.py import int_Set

#Lets create two 'sets' to test.
set_1 = int_Set()
set_2 = int_Set()

#Store values in set 1 and set 2.
for i in range(1,6):
    set_1.insert(i)     # Insert test 1

print("Insert Method Test 1.1: " + set_1)            # Quality Check
print("Should Contain Values 1 - 6.")

for i in range(3,9):
    set_2.insert(i)     # Insert test 1


print("Insert Method Test 1.2: " + set_2)            # Quality Check
print("Should Contain Values 3 - 9.")

#------------------------------------------------
# Test each method to ensure proper functionality
#------------------------------------------------

# Insert test 2
if set_1.insert(3):             # should return False
    print("Insert Method Pass test 2.1      :)")
else:    
    print("Insert Method Failed test 2.1    :(")

if not set_2.insert(9):        # should return True
    print("Insert Method Pass test 2.2      :)")
else:
    print("Insert Method Failed test 2.2    :(")