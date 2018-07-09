#1
try:
    a = 3
    if a<4:
        a = a/(a-3)
        print(a)
except Exception:
    print("error found")

#2
try:
    l = [1,2,3]
    print(l[3])

except Exception:
    print("error available")

#3
an exception

#4
-5.0
a/b result in 0

#5
import sys
 try:
    from time import datetime
 except Exception as e:
    print (e)
    print (sys.exc_type)

try:
int(5.6754) 
5
except ValueError:
print("error")

import sys
try:
my_list = [3,7, 9, 4, 6]
print my_list[6]
except IndexError as e:
print e
print sys.exc_type

 