def topten():
    n=1

    while n<=100:
        sq=n*n
        yield sq
        n=n+1


c=topten()

for i in c:
    print(i)