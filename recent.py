#Q1
i = input("Hello")
print (i)

#Q2
while True:
    print("Hello")

#Q3
list = []
 
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))
 
list.append(first)
list.append(second)
list.append(third)

print(list)

for first in list:
    print("square of first element is :", first*first)

#Q4
mylist = [4 , 'a' , 'b' , 'v' , 3.14 , 5]

myIntlist = [x for x in mylist if isinstance(x , int)]

myStringlist = [x for x in mylist if isinstance(x , str)]

myFloatlist = [x for x in mylist if isinstance(x , float)]
print(myIntlist)
print(myStringlist)
print(myFloatlist)

#Q5
even = []
 
for n in range(1,101):
    if n % 2 == 0:
        even.append(n)
 
for n in even:
	print(even)

#Q6
n = int(input('Enter number of lines '))
 
for i in range(1 , n+1):
	print ((n-i)*' '+i*'* ')

