#TODO phase1 and 2 don't need menus and can just be scripts
#use this to copy into phase3.py when we get there
#afterwards this can be deleted

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

#added here so I can copy and paste into phase 3 as needed
from bsddb3 import db
import sys
import re

termsDB = db.DB()
pdatesDB = db.DB()
pricesDB = db.DB()
adsDB = db.DB()
termsDB.set_flags(db.DB_DUP)
pdatesDB = set_flags(db.DB_DUP)
prices = db.DB()
adsDB = db.DB()
termsDB.open('te.idx', None, db.DB_BTREE)
pdatesDB.open('da.idx', None, db.DB_BTREE)
pricesDB.open('pr.idx', None, db.DB_TREE)
adsDB.open('ad.idx', None, db.DB_HASH)
termsCur = termsDB.cursor()
pdatesCur = pdatesDB.cursor()
pricesCur = pricesDB.cursor()
adsCur = adsDB.cursor()

equalityCheck = '='
rangeCheck = '[<=,>=,<,>]'
wordCheck = '[0-9a-zA-Z_-]+'
outputCheck = 'output='
equiSearch = re.compile(equalityCheck)
rangeSearch = re.compile(rangeCheck)
wordSearch = re.compile(wordCheck)
outputSearch = re.compile(outputCheck)
output = 0

def outputSet():

def generalCheck():

def equalityCheck():

def rangeCheck():

def queryCheck():

def StdInCheck():
    for each in sys.stdin:
        word = False
    
