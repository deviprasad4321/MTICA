def numbers(s):
    temp=''
    for i in s:
        #print("i=",i)
        if i in '0123456789':
            temp +=i
            #print("i:",i,"temp:",temp)
    return temp
str1=input()
a=numbers(str1)
print(a)
