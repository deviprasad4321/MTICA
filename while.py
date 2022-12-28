lst=[]
while(True):
    inp=int(input('enter the value(0 to end):'))
    if inp==0:
        break
    else:
        lst.append(inp)
lst.sort()
print('min:',lst[0])
print('max:',lst[-1])
print('avg:',round(sum(lst)/len(lst),1))
