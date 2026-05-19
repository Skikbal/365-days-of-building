class Car: # blueprint / bundle
    wheels = 4 # class attribute
    body= "metal"
    
    # constructor
    def __init__(self,color,make,model):
        self.color = color #public var # instance attribute
        self.__make = make # private var
        self._model = model # protected var
    # class methods
    def start(self):
        print("started")
        
    def stop(self):
        print("stopped")

Car1 = Car("red","bmw","X5")  # object
print(Car1.color)
print(Car1._Car__make) # its a private var cant access it outside the class
print(Car1._model) # its a warning that its a protected var dont access it outside the class.
Car1.start()
Car1.stop()