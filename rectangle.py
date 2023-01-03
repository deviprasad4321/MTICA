class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def peri(self):
        return 2*(self.length+self.breadth)
r=int(input('Enter the length:'))
t=int(input('Enter the breadth:'))
s=Rectangle(r,t)
print(s.area())
print(s.peri())
