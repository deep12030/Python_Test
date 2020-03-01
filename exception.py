a=4
b=2
try:
    print("resource open")
    print(a/b)

    k=int(input("enter a number"))
    print(k)

#except Exception as e:
except ZeroDivisionError as e:
        print("hey you cannot divide the number by zero",e)
except ValueError as e:
    print("invald input")
except Exception as e:
    print("something wrong")

finally:
    print("resource close")

