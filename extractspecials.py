def specials(s):
    temp=''
    for i in s:
        #print("i=",i)
        if i not in 'AEIOUaeiouBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz0123456789':
            temp +=i
            #print("i:",i,"temp:",temp)
    return temp
str1=input()
a=specials(str1)
print(a)
