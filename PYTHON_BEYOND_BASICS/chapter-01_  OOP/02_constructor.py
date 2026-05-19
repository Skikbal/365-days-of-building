class MyClass:
    var1 = "ikbal"
    var2 = "ali"
    
    def __init__(self,dyn1,dyn2,dyn3):
        #Instance variables
        self.dyn1 = dyn1
        self.dyn2 = dyn2
        self.dyn3 = dyn3
    def func1(self):
        print(f"hello world, {self.dyn1}")
    
    def func2(self):
        print(f"hello world, {self.dyn2}")
        
    def func3(self):
        print(f"hello world, {self.dyn3}")        
        
        
obj = MyClass("Ansh","Ali","Bal")
obj.func1()
        