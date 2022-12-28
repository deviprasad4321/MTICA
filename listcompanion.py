##lst=[]
##inp=input()
##for i in inp:
##    if i not in'aeiouAEIOU':
##        lst.append(i)
##print(*lst)
##
##ans=[i for i in inp if i not in 'AEIOUaeiou' ]
##print(''.join(ans))

string='today is tuesday'
##ans=[]
##wordslist=string.split(' ')
##for i in wordslist:
##    if len(i)<5:
##        ans.append(i)
##print(*ans)
wordslist=string.split(' ')
ans=[i for i in wordslist if len(i.strip('\n'))==5]
print(*ans)
 
