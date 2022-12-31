fo=open(r"D:\pythonpractice11\day9\new1.txt","a")
for i in range(5):
    inp=input('Enter text:')
    fo.write(inp+'\n')
fo.close()
print('Text written to file')
