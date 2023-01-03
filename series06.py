def printSeries(n):
    if n<0:
        print( 'INVALID')
    else:
        for i in range(1,n+1):
            num=1
            print()
            for j in range(i):
                print(num,end=' ')
                num+=1
inp=int(input())
printSeries(inp)

               
