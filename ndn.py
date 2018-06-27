#Q1
year = 2008
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#Q2
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
 
print()

#Q3
print("enter first age")
first = input()
print("enter second age")
second = input()
print("enter third age")
third = input()

if first >= second and first >= third:
    print("oldest is:", first)
elif second >= first and second >=third:
    print("oldest is:", second)
elif third >= first and third >= second:
    print("oldest is:", third)
else:
    print("all are equal")
    

#Q5
print("enter quantity")
quantity = input()
if quantity*100 > 1000:
    print("cost is",((quantity*100)-(0.1*quantity*100))
else:
    print("cost is ",quantity*100)


