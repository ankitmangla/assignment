#1
class Animal:
    def Animal_attribute(self,habitat,t):
        print(habitat)
        print(t)

class Tiger(Animal):
    def Tiger_attribute(self,food):
        print(food)
        
x = Tiger()
x.Tiger_attribute('deer')
x.Animal_attribute('forest','wild')

#2
AB
AB

#3
class cop:
    def __init__(self,name,age,experience,designation):
        self.name = name
        self.age = age
        self.experience = experience
        self.designation = designation
    def add(self):
        print("add your details", self.name)

    def display(self):
        print(self.name)
        print(self.age)
        print(self.experience)
        print(self.designation)

    def update(self,name,age,experience,designation):
        self.name = name
        self.age = age
        self.experience = experience
        self.designation = designation
class mission(cop):
    def add_mission_details(self,missions):
        print("the following %s is assigned to %s"%(mission,self.name))

#Q4
class shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
print(a.area())

class rectangle(shape):
    a = rectangle(6,4)
    print a.area()

class square(shape):
    b = square(5,5)
    print b.area()
    
        

    
    
