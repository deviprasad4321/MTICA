string='''
practice problems for list com pre hension in python.
'''
wordlist=string.split(' ')
print(wordlist)
wordlist=[i.strip("\n") for i in wordlist ]
print(wordlist)
ans={i:len(i) for i in wordlist }
print(ans)


string='''
practice problems for list com pre hension in python.
'''
wordlist=string.split(' ')
##print(wordlist)
wordlist=[i.strip("\n") for i in wordlist ]
##print(wordlist)
ans={i:i[::-1] for i in wordlist }
print(ans)

lst=[]
for i in range(1,101):
    if i%2==0 or i%3==0 or i%4==0 or i%5==0 or i%6==0 or i%7==0 or i%8==0 or i%9==0:
        lst.append(i)
print(*lst)


lst=[]
for i in range(1,101):
    for j in range(2,10):
        if i%j==0:
            lst.append(i)
            break
print(*lst)



lst=[]
for i in range(100,111):
    temp=[]
    for j in range(1,10):
        if i%j==0:
            temp.append(j)
    lst.append([i,max(temp)])
print(*lst)

ans=[]
for i in range(100,111):
    ans.append([i,max([j for j in range(1,11) if i%j==0])])
print(ans)


ans=[[i,max([j for j in range(1,11) if i%j==0])]for i in range(100,111)]
print(ans)


#find the transpose of a matrix
##m=[[1,2],[3,4],[5,6],[7,8]]
##ans=[]
##for row in range(len(m[0])):
##    temp=[]
##    for col in range(len(m)):
##        temp.append(m[col][row])
##    ans.append(temp)
##print(ans)


##m=[[1,2],[3,4],[5,6],[7,8]]
##ans=[]
##for row in range(len(m[0])):
##    temp=[m[col][row] for col in range(len(m))]
##    
##    ans.append(temp)
##print(ans)

##m=[[1,2],[3,4],[5,6],[7,8]]
##ans=[]
##for row in range(len(m[0])):
##    
##    ans.append([m[col][row] for col in range(len(m))])
##print(ans)



##m=[[1,2],[3,4],[5,6],[7,8]]
##ans=[[m[col][row] for col in range(len(m))] for row in range(len(m[0])) ]
##
##print(ans)


##lst=[]
##for i in range(1200,2000,130):
##    lst.append(i)
##print(lst)

##ans=[i for i in range(1200,2001,130)]
##print(ans)


##lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in lst:
##    ans.append(i+6)
##print(ans)
    
##lst=[10,15,20,25,30,35,40,45]
##ans=[(i+6) for i in lst]
##print(ans)

##lst=[10,15,20,25,30,35,40,45]
##ans=[(i*i) for i in lst]
##print(ans)


##square root
##lst=[10,15,20,25,30,35,40,45]
##ans=[(i**0.5) for i in lst]
##print(ans)

##lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in lst:
##    ans.append(round(i**0.5,4))
##print(ans)


##lst=[10,15,20,25,30,35,40,45]
##ans=[]
##for i in lst:
##    if (i*i)>50:
##        ans.append(i*i)
##print(ans)


##lst=[10,15,20,25,30,35,40,45]
##ans=[(i*i) for i in lst if (i*i)>50 ]
##print(ans)



##dict1={'sedan':100,'ratan':1022,'matan':5001}
##lst=[]
##for i in dict1:
##    if dict1[i]<5000:
##        lst.append(i.upper())
##print(lst)


##dict1={'sedan':100,'ratan':1022,'matan':5001}
##lst=[i.upper() for i in dict1 if dict1[i]<5000]
##print(lst)       




##for i in range(4):
##    inp=input()
##    if inp:
##        print("Hello "+inp+" !")
##    else:
##        print("chalo")


##lst=[10,20,30,40,50,6,70,80,90]
##import math
##print(lst)
##result=list(map(math.sqrt,lst))
##print(result)










































