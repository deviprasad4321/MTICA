def printSun():
    print('SUNDAY\n')
    return
def printMon():
    print('MONDAY\n')
    return
def printTue():
    print('TUESDAY\n')
    return
def printWed():
    print('WEDNESDAY\n')
    return
def printThu():
    print('THURSDAY\n')
    return
def printFri():
    print('FRIDAY\n')
    return
def printSat():
    print('SATURDAY\n')
def choice():
    print('Enter the day number between 1-7:')
DaySelect={1:printSun,2:printMon,3:printTue,
           4:printWed,5:printThu,6:printFri,
           7:printSat}
selection=0
while(True):
    if selection>7:break
    choice()
    selection=int(input('Selection the option:'))
    if(selection>=1) and (selection<8):
        DaySelect[selection]()
                  
