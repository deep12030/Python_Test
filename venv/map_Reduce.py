from functools import reduce

nums=[1,2,3,4,5,6,7,8]
filter=list(filter(lambda a:a%2==0,nums))
doubles=list(map(lambda a:a*a,filter))
sum=reduce(lambda a,b:a+b,doubles)
print(filter)
print(doubles)
print(sum)