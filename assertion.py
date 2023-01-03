class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        assert(self.num2!=0), "number is not divisible by 0"
        return self.num1/self.num2
n1=int(input())
n2=int(input())
ob=Number(n1,n2)

print(n1,'+',n2,'=',ob.add())
print(n1,'-',n2,'=',ob.sub())
print(n1,'*',n2,'=',ob.mul())
try:
    print(n1,'/',n2,'=',ob.div())
except AssertionError as ad:
    print(ad)
