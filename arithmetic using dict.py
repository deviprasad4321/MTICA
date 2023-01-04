def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMul(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print('+:Addition\n''-:Substraction\n''*:Multiplication\n''/:Division\n''Press any other key to exit\n')
Select={'+':printAdd,'-':printSub,'*':printMul,'/':printDiv}
choice()
while(True):
    i=input('Enter the option:')
    if i=='+' or i=='-' or i=='*' or i=='/':
        j=int(input('Enter the value for a:'))
        k=int(input('Enter the value for b:'))
        l=Select[i](j,k)
        print(j,i,k,'=',l)
    else:
        print('EXIT complete')
        break
              
