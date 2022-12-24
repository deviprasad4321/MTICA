def armstrong(num):
    num=str(num)
    n=len(num)
    total=0
    for i in num:
        total +=int(i)**n
    if int(num)==total:
        return 1
    else:
        return 0
inp=int(input())
if armstrong(inp):
    print("YES")
else:
    print("NO")
