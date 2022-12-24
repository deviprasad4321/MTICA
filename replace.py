def replace(n):
    n=n.replace('3','.')
    n=n.replace('5','3')
    n=n.replace('.','5')
    return n
inp=int(input())
inp=str(inp)
print(replace(inp))

