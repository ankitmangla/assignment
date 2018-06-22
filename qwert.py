#Q1
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return self.radius*2*3.14

NewCircle = Circle(5)
print(NewCircle.area())
print(NewCircle.perimeter())


# Q2
class student():
    def__init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print self.name
        print self.roll
    def setAge(self,age):
        self.age = age
    def setMarks(self,marks):
        self.marks = marks

#Q3                    
class temperature():
    def convertfahrenheit(self, celsius):
        return (celsius*(9/5))+32
    def convertcelsius(selg, fahrenheit):
        return (fahrenheit-32)*(5/9)
#Q4
class MovieDetails():
    def__init__(self, mn, an, yor, rating):
        self.moviename = mn
        self.artistname = an
        self.year_of_release = yor
        self.rating = rating

    run = MovieDetails(run, shahid, 2010, 3)
    print(run.artistname)

# Q5
class salary():
    def__init__(self, expenditure, savings):
        self.expenditure = expenditure
        self.savings = savings
ankit = salary(25000, 15000)
print("ankit")
