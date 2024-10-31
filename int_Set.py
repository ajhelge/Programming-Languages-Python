# A remake of the set class given by python. This one only supports ints and is created using lists.
#Author: Alec Helgeson

class int_Set():

    def __init__(self):
        self.setList = []
        self.size = 0

    def insert(self, int_To_Insert):            # Returns true if successful, false otherwise.
        if int_To_Insert not in self.setList:
            self.setList.append(int_To_Insert)
            return True
        return False

    def remove(self, int_To_Remove):            # Returns true if successful, false otherwise.
        if int_To_Remove in self.setList:
            self.setList.remove(int_To_Remove)
            return True
        return False

    def isMember(self, int_To_Check):           # Check if int is in set.
        if int_To_Check in self.setList:
            return True
        return False

    def isSubset(self, set_To_Check):           # Check if every member in set 2 is in set 1, if so, return true.
        for item in set_To_Check:
            if item not in self.setList:
                return False
        
        return True
            
    def Intersect(self, set_To_Intersect):
        pass
    def Union(self, set_To_Union):
        pass
    def Diff(self, set_To_Diff):
        pass
    def __str__(self):
        pass