class Doodad:
    def __init__(self, name, age, DOB, sex):
        self.name = name
        self.age = age
        self.date_of_birth = DOB
        self.sex = sex 
    
person1 = Doodad("Callie", "17", "Feb. 29th", "Female")

print(person1.name)

#Always defined by dots