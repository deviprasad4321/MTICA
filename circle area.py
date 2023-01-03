class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14159*self.radius**2
    def peri(self):
        return 2*3.14*self.radius
r=int(input('Enter the Radius:'))
s=Circle(r)
print(s.area())
print(s.peri())
                 
