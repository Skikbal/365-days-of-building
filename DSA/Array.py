# import array as a
from array import *

arr = array('i',[1,2,3,4,5,6])
print(len(arr))
for i in range(0,len(arr)):
    print(arr[i],end= " ")

print('\n')
for x in arr:
    print(x,end=",")
    
print('\n')
    
print(arr.typecode)
rev = arr
rev.reverse()
for x in rev:
    print(x,end=",")