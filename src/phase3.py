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

def generalCheck(keyword):
        #key word search in title and description
        # find the key word in terms.idx, return all ad id, display all ads associated with ad ids
        
def equalityCheck():
        #location and category search, exact matching to keyword

def rangeCheck():
        # price and data search, also includes equality

def queryCheck():

def StdInCheck():
    for each in sys.stdin:
        word = False
    

