def vowel(s):
    temp=''
    for i in s:
        print("i=",i)
        if i in 'AEIOUaeiou':
            temp +=i
            print("i:",i,"temp:",temp)
    return temp
str1=input()
a=vowel(str1)
print(a)
