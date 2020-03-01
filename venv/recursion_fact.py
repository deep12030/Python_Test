def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
r=4
x=fact(r)
print(x)