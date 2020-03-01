class car:
    wheels=5
    def __init__(self):
        self.com="audi"
        self.mil=8
c1=car()
c2=car()
c1.mil=10
car.wheels=4

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
