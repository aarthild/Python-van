class Human:
    def __init__(self):
        self.x=0
        self.y=0
        print("Hai")
    def Increment(self):
        self.x=self.givevalue()+1
    def givevalue(self):
        return self.y
Thub=Human()
Thub.Increment()
print(Thub.x)

