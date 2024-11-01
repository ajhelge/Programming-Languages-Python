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
            
    def Intersect(self, set_To_Intersect):      #returns an intersection of set 1 and set 2 (only items in both).
        set_I = int_Set()
        for item in set_To_Intersect:
            if item in self.setList:
                set_I.insert(item)
        
        for item in self.setList:
            if item in set_To_Intersect:
                set_I.insert(item)
        
        return set_I

    def Union(self, set_To_Union):              # Returns an Union of set 1 and set 2 (All items in both).
        set_U = int_Set()
        for item in self.setList:
            set_U.insert(item)
        for item in set_To_Union:
            set_U.insert(item)

        return set_U
    
    def Diff(self, set_To_Diff):                # Returns the difference between set 1 and set 2 (set 1 minus set 2).
        set_D = int_Set()
        for item in self.setList:
            if item not in set_To_Diff:
                set_D.insert(item)

        return set_D
    
    def __str__(self):                          #Returns the contents of a set in a formatted string
        return "{" + ", ".join(str(item) for item in self.setList) + "}"