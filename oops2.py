class car:
    def __init__(self):
        self.colour="black"
        self.seats="7seater"
        print(self.colour)
        print(self.seats)
        self.speed=40
    def accelerate(self):
        self.speed=self.speed+10
        return self.speed
    def brake(self):
        self.speed=self.speed-10
        return self.speed
audi=car()
print(audi.accelerate())

    
