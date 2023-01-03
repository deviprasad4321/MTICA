def printSeries(ch,n):
    sp='.'
    if n<0:
        print( 'INVALID')
    else:
        for i in range(0,n):
            print(sp*(n-i-1)+ch*(2*i+1)+sp*(n-i-1))
    return None
inpn=input()
inp=int(input())

printSeries(inpn,inp)
