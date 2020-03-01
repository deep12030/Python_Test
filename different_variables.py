class students():
    school="elte"
    def __init__(self,m1,m2,m3,m4):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
    def avg(self):
        return(self.m1+self.m2+self.m3+self.m4)/4
    def results(self):
        if res>=4:
            print("passed")
        else:
            print("failed")

    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def info():
        print("welcome t0 orientation day!!")



c1=students(2,3,4,5)
c2=students(2,3,6,9)
res=c1.avg()
print(res)
print(students.get_school())
students.info()
