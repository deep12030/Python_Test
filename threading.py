
from threading import *
from time import sleep

class hello(threading):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class hi(td.thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
t1=hello()
t2=hi()
t1.start()
sleep(0.5)
t2.start()
print("thread")