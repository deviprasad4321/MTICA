def decitobin(n):
    n=bin(n)[2:]
    return n
inp=int(input())
binary=decitobin(inp)
print(binary)
