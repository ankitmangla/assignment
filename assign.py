# Q1
pi = 3.14
radius = float(input("Enter the radius of the circle :"))
area = pi*radius*radius
print("the area of circle is %.2f" %area)

# Q2
limit = int(input("Enter upper limit for perfect number search: "))

n = 1

while n <= limit:

    sum = 0
    divisor = 1
    while divisor < n:
        if not n% divisor:
            sum+= divisor
        divisor = divisor + 1
        
        if sum == n:
            print(n, "is a perfect number")
        n = n + 1

# Q3
def multable(n, i = 1):
    print(n*i)
    if i != 10:
        multable(n, i+1)
        multable(12)
    
# Q4
def power(base, exp):
    if(exp ==1):
        return(base)
    if(exp !=0):
        return(base*power(base, exp-1))
base = int(input("Enter base value:"))
exp = int(input("Enter exponent value:"))
print("Result:",power(base, exp))

# Q5
def fact(n):
    if(n <= 1):
        return 1
    else:
        return(n*fact(n-1))
n = int(input("Enter the number:"))
print("Factorial:")
print(fact(n))
