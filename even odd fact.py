import math
class Number:
    def __init__(self,num):
        self.num=num
    def fact(self):
        a=1
        for i in range(1,self.num+1):
            a=a*i
        return a
    def even(self):
        if self.num%2==0:
            return 'EVEN NUMBER'
        else:
            return 'ODD NUMBER'
    def sum(self):
        str1=str(self.num)
        c=0
        for i in str1:
            c=c+int(i)
        return c
    def arm(self):
        d=0
        str2=str(self.num)
        for i in str2:
            d+=math.pow(int(i),len(str2))
        if int(self.num)==d:
            return "ARMSTRONG NUMBER"
        else:
            return "NOT ARMSTRONG NUMBER"
    def prime(self):
        if self.num<1:
            return 'INVALID'
        if self.num==1 or self.num==2 or self.num==3:
            return 'PRIME NUMBER'
        for i in range(2,self.num):
            if self.num%i==0:
                return 'NOT PRIME NUMBER'
        return 'PRIME NUMBER'
        
            
            
    
r=int(input('Enter the number:'))
s=Number(r)
print('The factorial of',r,'is',s.fact())
print(r,'is a',s.even())
print('The sum of the given input',r,'is',s.sum())
print(r,'is a',s.arm())
print(r,'is a',s.prime())








