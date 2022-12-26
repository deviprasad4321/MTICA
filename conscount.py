def conscount(s):
    con=0
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            con+=1
    return con
str1=input()
a=conscount(str1)
print("no of consonants in a'",str1,"'is",a)
