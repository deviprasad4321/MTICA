def printWeek(n):
    switcher={
    1:'sunday',
    2:'monday',
    3:'tuesday',
    4:'wednesday',
    5:'thursday',
    6:'friday',
    7:'saturday',
    }
    return switcher.get(n,'invalid')
def printMonth1(n):
    if n==1:
        return 'sunday'
    elif n==2:
        return 'monday'
    elif n==3:
        return 'tuesday'
    elif n==4:
        return 'wednesday'
    elif n==5:
        return 'thursdayy'
    elif n==6:
        return 'friday'
    elif n==7:
        return 'saturday'
    else:
        return 'invalid'
import time
for i in range(8):
    inp=int(input())
    start=time.time()
    print(printWeek(inp))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printMonth1(inp))
    print((time.time()-start)*10000000)









    
