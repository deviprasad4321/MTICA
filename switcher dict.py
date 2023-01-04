def printBlue():
    print('u choose blue\n')
    return
def printRed():
    print('u choose red\n')
    return
def printOrange():
    print('u choose Orange\n')
    return
def printYellow():
    print('u choose Yellow\n')
    return
def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return
ColourSelect={0:printBlue,1:printRed,2:printOrange,3:printYellow}
selection=0
while(True):
    if selection==4:break
    choice()
    selection=int(input('Select a colour option:'))
    if(selection>=0) and (selection<4):
        ColourSelect[selection]()
    
    
