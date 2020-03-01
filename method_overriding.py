class parent:
    def show(self):
        print("in parent")
class child(parent):
    def show(self):
        print("in child")

a=child()
a.show()