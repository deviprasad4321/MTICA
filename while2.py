lst1=[]
lst2=[]
while(True):
    inp=int(input('enter the even or odd:'))
    if inp<0:
        break
    elif(inp%2==0):
        lst1.append(inp)
    else:
        lst2.append(inp)
lst1.sort()
print('EVEN:',*lst1)
print('min:',lst1[0])
print('max:',lst1[-1])
print('avg of even:',round(sum(lst1)/len(lst1),1))
lst2.sort()
print('ODD:',*lst2)
print('min:',lst2[0])
print('max:',lst2[-1])
print('avg of odd:',round(sum(lst2)/len(lst2),1))
