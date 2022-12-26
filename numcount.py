def numbercount(s):
    num=0
    for i in s:
        if i in '0123456789':
            num+=1
    return num
str1=input()
a=numbercount(str1)
print("no of numbers in a'",str1,"'is",a)
