def printMonth(n):
    if n==1:
        return 'january'
    if n==2:
        return 'february'
    if n==3:
        return 'march'
    if n==4:
        return 'april'
    if n==5:
        return 'may'
    if n==6:
        return 'june'
    if n==7:
        return 'july'
    if n==8:
        return 'august'
    if n==9:
        return 'september'
    if n==10:
        return 'october'
    if n==11:
        return 'november'
    if n==12:
        return 'december'
    else:
        return 'invalid input'
def printMonth1(n):
    if n==1:
        return 'january'
    elif n==2:
        return 'february'
    elif n==3:
        return 'march'
    elif n==4:
        return 'april'
    elif n==5:
        return 'may'
    elif n==6:
        return 'june'
    elif n==7:
        return 'july'
    elif n==8:
        return 'august'
    elif n==9:
        return 'september'
    elif n==10:
        return 'october'
    elif n==11:
        return 'november'
    elif n==12:
        return 'december'
    else:
        return 'invalid input'
import time
for i in range(4):
    inp=int(input())
    start=time.time()
    print(printMonth(inp))
    print(time.time()-start)
    start=time.time()
    print(printMonth1(inp))
    print(time.time()-start)
    
    
