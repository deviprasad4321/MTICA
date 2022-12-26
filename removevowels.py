def vowel(s):
    temp=''
    for i in s:
       # print("i=",i)
        if i not in 'AEIOUaeiou':
            temp +=i
           # print("i:",i,"temp:",temp)
    return temp
str1=input()
a=vowel(str1)
print(a)




##def vowelcount(s):
##    vowel=0
##    for i in s:
##        if i in 'AEIOUaeiou':
##            vowel+=1
##    return vowel
##str1=input()
##a=vowelcount(str1)
##print("no of vowels in a'",str1,"'is",a)
##





