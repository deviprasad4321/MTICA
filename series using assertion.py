def seriesincrease(ch,n):
    assert isinstance(ch,str),"first argument should be string"
    assert isinstance(n,int),"second argument should be int"
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def seriesdecrease(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None
inp=input('enter a character:')
inpn=int(input('enter a number:'))
try:
    seriesincrease(inp,inpn)
except AssertionError as ob:
    print(ob)
    print('-'*40)
seriesdecrease(inp,inpn)
