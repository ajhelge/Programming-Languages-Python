from int_Set import int_Set

print("\n")
print("-------------------------------------------------")
print("      Initialize three sets to run tests on")
print("-------------------------------------------------")
set_1 = int_Set()
set_2 = int_Set()
set_3 = int_Set()

#Store values in set 1 and set 2.
for i in range(1,7):
    set_1.insert(i)                                 # Insert test 1

print("Insert Method Test 1.1: ", end="")           # Quality Check
print(set_1)
print("Should Contain Values 1 - 6.\n")

for i in range(4,10):
    set_2.insert(i)                                 # Insert test 1

print("Insert Method Test 1.2: ", end="")           # Quality Check
print(set_2)
print("Should Contain Values 4 - 9.\n")

for i in range(2,4):
    set_3.insert(i)                                 # Insert test 1

print("Insert Method Test 1.3: ", end="")           # Quality Check
print(set_3)
print("Should Contain Values 2 and 3.")

#--------------------------------------------------------
print()
print("-------------------------------------------------")
print("            Functionality Testing")
print("-------------------------------------------------")
# Insert test 2.1
if not set_1.insert(3):                             # Tests to make sure you cannot insert an already existing value, should return False
    print("Insert Method test 2.1:               Pass :)")
else:    
    print("Insert Method test 2.1:               Fail :)")

# Insert test 2.2
if not set_2.insert(9):                             # Tests to make sure you cannot insert an already existing value, should return False
    print("Insert Method test 2.2:               Pass :)")
else:
    print("Insert Method test 2.2:               Fail :)")

# Remove test 3.1
if set_1.remove(1):
    if 1 not in set_1.setList:
        print("Remove Method test 3.1:               Pass :)")
else:
    print("Remove Method test 3.1:               Fail :(")
set_1.insert(1) # Replace missing value

# Remove test 3.2
if not set_2.remove(3):
    print("Remove Method test 3.2:               Pass :)")
else:
    print("Remove Method test 3.2:               Fail :(")


# isMember test 4.1
if set_1.isMember(1):
    print("isMember Method test 4.1:             Pass :)")
else:
    print("isMember Method test 4.1:             Fail :(")

# isMember test 4.2
if set_2.isMember(4):
    print("isMember Method test 4.2:             Pass :)")
else:
    print("isMember Method test 4.2:             Fail :(")

print("-------------------------------------------------")
print("             Set Operation Testing")
print("-------------------------------------------------")

# isSubset test 5.1
if not set_1.isSubset(set_2.setList):
    print("isSubset Method test 5.1:             Pass :)")
else:
    print("isSubset Method test 5.1:             Fail :(")

# isSubset test 5.2
if set_1.isSubset(set_3.setList):
    print("isSubset Method test 5.2:             Pass :)")
else:
    print("isSubset Method test 5.2:             Fail :(")

# Intersect test 6.1
set_temp = set_1.Intersect(set_2.setList)
if (set_1.isSubset(set_temp.setList) and set_1.isSubset(set_temp.setList)):
    print("Intersect Method test 6.1:            Pass :)")
else:
    print("Intersect Method test 6.1:            Fail :(")

# Intersect test 6.2
set_temp = set_1.Intersect(set_3.setList)
if set_1.isSubset(set_temp.setList) and set_3.isSubset(set_temp.setList):
    print("Intersect Method test 6.2:            Pass :)")
else:
    print("Intersect Method test 6.2:            Fail :(")

# Union test 7.1
set_temp = set_1.Union(set_2.setList)
if set_temp.isSubset(set_1.setList) and set_temp.isSubset(set_2.setList):
    print("Union Method test 7.1:                Pass :)")
else:
    print("Union Method test 7.1:                Fail :(")

# Union test 7.2
set_temp = set_1.Union(set_3.setList)
if set_temp.isSubset(set_1.setList) and set_temp.isSubset(set_3.setList):
    print("Union Method test 7.2:                Pass :)")
else:
    print("Union Method test 7.2:                Fail :(")

# Difference test 8.1       (not exactly a precise way to test, needs to be better #TODO)
set_temp = set_1.Diff(set_2.setList)
if set_1.isSubset(set_temp.setList) and not set_temp.isSubset(set_2.setList):
    print("Difference Method test 8.1:           Pass :)")
else:
    print("Difference Method test 8.1:           Fail :(")

# Difference test 8.2       (not exactly a precise way to test, needs to be better #TODO)
set_temp = set_1.Diff(set_3.setList)
if set_1.isSubset(set_temp.setList) and not set_temp.isSubset(set_3.setList):
    print("Difference Method test 8.2:           Pass :)")
else:
    print("Difference Method test 8.2:           Fail :(")



print("-----------------end of testing------------------\n")