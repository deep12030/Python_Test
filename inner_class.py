class students:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.comp="hp"
            self.ram=400
            self.cpu="i5"
        def show(self):
            print(self.comp,self.ram,self.cpu)


s1=students("deepak",1)
s2=students("soni",2)
s1.show()
s2.show()