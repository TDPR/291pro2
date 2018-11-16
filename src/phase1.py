#Preparing Data Files

from bsddb3 import db

def phase1Menu():
    print('Control the menu using numbers')
    print('1. Insert Data Files')
    print('2. Return to the main menu')
    res=input()

    if res == '1':
        dataInput()
    
    elif res == '2':
        print('\n')
        from index import mainMenu
        mainMenu()
    
    else:
        print('\nInvalid Input')
        phase1Menu()


def dataInput():
    print('Hello World')
