class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram



    def config(self):
         print("configuration is",self.cpu,self.ram)
com1=computer("i5",15)
com2=computer("i7",10000)

#computer.config(com1)
#computer.config(com2)
com1.config()
com2.config()