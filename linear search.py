pos=-1
def search(lsit,n):
    i=0
    while i<len(list):

        if list[i]==n:
            print("found here")
            globals()['pos']=i
            return True
        i=i+1
    return False






list=[1,2,3,4,5,78,8,44]
n=44
if search(list,n):
    print("found",pos+1)
else:
    print("not found")