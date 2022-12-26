def specialcount(s):
    special=0
    for i in s:
        if i not in 'AEIOUaeiouBCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz0123456789':
            special+=1
    return special
str1=input()
a=specialcount(str1)
print("no of specialcharacters in a'",str1,"'is",a)
