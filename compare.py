class computer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def compare(self,other):
        if self.age==other.age:
            print("same")
        else:
            print("different")
    def update(self):
         self.age=100
    def prize(self):
        if self.age==100:
            print("congratulations")
        else:
            print("try next time")



com1=computer("deepak",27)
com2=computer("kaustubh",25)
com1.update()
com1.prize()

com1.compare(com2)