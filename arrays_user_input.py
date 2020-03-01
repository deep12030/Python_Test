from array import *
arr=array('i',[])
n=int(input("enter the size of array "))

for i in range(n):
    x=int(input("the entered value is: "))
    arr.append(x)
print(arr)

val=int(input("enter the elements to be searched: "))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1
print(arr.index(val))
