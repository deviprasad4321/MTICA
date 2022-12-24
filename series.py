def series(n):
    tem=[]
    for i in range(n+1):
        tem.append(i)
    return tem
inp=int(input())
ans=series(inp)
print(*ans)
print(sum(ans))
