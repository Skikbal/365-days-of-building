class car: # blueprint / bundle
    wheels = 4 # class attribute
    body= "metal"
    
    # constructor
    def __init__(self,color,make):
        self.color = color # instance attribute
        self.make = make
    # class methods
    def start(self):
        print("started")
        
    def stop(self):
        print("stopped")

car1 = car("red","bmw")  # object
print(car1.color)
print(car1.make)
car1.start()
car1.stop()