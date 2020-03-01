
pos=1
def search(list,n):
    i=0
    for i in list:
        if list[i]==n:
            print("found here")
            globals()['pos']=i
            return True
    return False


# creating an empty list
list = []

# number of elemetns as input
a = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, a):
    ele = int(input())

    list.append(ele)  # adding the element

print(list)


n=int(input("enter the number to be searched: "))


if search(list,n):
    print("found",n,pos+1)
else:
    print("not found")