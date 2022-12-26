def vowelcount(s):
    vowel=0
    for i in s:
        if i in 'AEIOUaeiou':
            vowel+=1
    return vowel
str1=input()
a=vowelcount(str1)
print("no of vowels in a'",str1,"'is",a)



