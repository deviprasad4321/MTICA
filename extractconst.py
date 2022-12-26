def consonant(s):
    temp=''
    for i in s:
        #print("i=",i)
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            temp +=i
            #print("i:",i,"temp:",temp)
    return temp
str1=input()
a=consonant(str1)
print(a)