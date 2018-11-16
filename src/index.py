#TODO phase1 and 2 don't need menus and can just be scripts

def mainMenu():
    print('Control the menu using numbers')
    print('1. Prepare Data Files')
    print('2. Build Indexes')
    print('3. Retrieve Data')
    print('4. Exit')
    res=input()

    if res == '1':
        #call phase1.py
        mainMenu()
    elif res == '2':
        #call phase2.py
        mainMenu()
    elif res == '3':
        #call phase3.py
        mainMenu()
    elif res == '4':
        print('\nGoodbye')
        exit()
    else:
        print('\nInvalid Input')
        mainMenu()


if __name__ == '__main__':
    print('Mini Project 2')
    print('By maoued, sandare, tdr')

mainMenu()
