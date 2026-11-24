class Myclass:
    
    def display(self,x):
        self.x=x
        print("The value of x is",x)

    def vinay(self):
        print("hello vinay")
        
obj=Myclass()
obj.display(5)
print(obj.x)
obj.vinay()
