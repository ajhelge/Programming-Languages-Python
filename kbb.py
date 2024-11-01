class vehicle():

    def __init__(self):
        color = "black"
        engineConfig = "V6"
        make = "Audi"
        model = "A6"
        year = "2012"
        mileage = 150000

    def appraise(self):
        #Generic vehicle questions to fill attributes would go here.
        pass

class car(vehicle):

    def __init__(self):
        #car specific attributes go here
        #Examples: carType, fwd, rwd, awd.
        pass
    
    def appraise(self):
        #Generic car questions to fill attributes would go here.
        pass

class sedan(car):

    def __init__(self):
        #sedan specific attributes go here.
        pass

    def appraise(self):
        #Sedan specific questions to fill attributes would go here.
        pass

class coupe(car):
    
    def __init__(self):
        #Coupe specific attributes go here.
        pass

    def appraise(self):
        #Coupe specific questions to fill attributes would go here.
        pass

class truck(vehicle):

    def __init__(self):
        #truck specific attributes go here
        #Examples: tow package, cab size (standard, extended, crew, super)
        pass

    def appraise(self):
        #Generic truck questions to fill attributes would go here.
        pass

class lightTruck(truck):

    def __init__(self):
        #light truck specific attributes go here (light trucks are typically half ton and three quarter ton)
        #
        pass

    def appraise(self):
        #Light truck specific questions to fill attributes would go here.
        pass

class classicLightTruck(truck):

    def __init__(self):
        #Classic specific attributes go here
        #Examples: Diverced Transfercase, Axles make and model.
        pass

    def appraise(self):
        #Classic truck specific questions go here.
        pass

class mediumTruck(truck):

    def __init__(self):
        #medium truck specific attributes go here (medium trucks are typically one ton and two ton pickups).
        #Examples: fifth wheel hookups, dually (yes or no).
        pass

    def appraise(self):
        #Medium truck specific questions to fill attributes would go here.
        pass

class heavyTruck(truck):
    
    def __init__(self):
        #Heavy truck specific attributes go here (heavy trucks are typically the size of a semi and used commercially).
        #Examples: 
        pass

    def appraise(self):
        #Heavy truck specific questions to fill attributes would go here.
        pass