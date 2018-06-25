# Q1
list = ['apple','mango','banana','litchi']
print(list)

# Q2
list = ['apple','mango','banana','litchi']
list1=[]
for i in range(0,5):
    element = input("enter the element")
    list.append(element)
print(list)

# Q3
fruits = ['apple','mango','litchi','mango','banana']
print(fruits.count('mango'))

# Q4
l=[2,5,4,3,1,8,9,7]
l.sort()
a=list(l)
print(a)

# Q5
A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = A + B
C.sort()
D = list(C)
print(D)
