dict1={'sedan':100,'ratan':1022,'matan':5001}
lst=[]
for i in dict1:
    if dict1[i]<5000:
        lst.append(i.upper())
print(lst)
