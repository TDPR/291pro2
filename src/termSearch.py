# takes input of a list of length 1, or length 2 if modulo
import re
from bsddb3 import db
def termSearch(keyword):
    #open the data bases we will use
    termsBase = db.DB()
    termsBase.open('terms.idx', None, db.DB_BTREE)
    tcur = termsBase.cursor()
    adBase = db.DB()
    adBase.open('ads.idx')
    acur = adBase.cursor()
    # working lists
    outputList = []
    idList = []

    # index 0 is reserved for the keyword
    # index 1 is reserved for modulo, if it exists
    if len(keyword) == 1:
        keyword[0] = keyword[0].encode('utf-8') #necessary to match the db
        iter = tcur.get(keyword[0], db.DB_SET)
        while iter:
            print(iter)
            if iter[0] == keyword[0]:
                idList.append(iter[1])
            iter = tcur.next()
        for id in idList:
            ad = acur.get(id, db.DB_SET)
            outputList.append(ad)
        termsBase.close()
        adBase.close()
        print(idList)
        return print(outputList) #####
    
    elif len(keyword) == 2:
        iter = tcur.first()
        while iter:
            key = iter[0].decode()
            key = key+'*'
            if re.search(keyword, key):
                idList.append(iter[1])
            iter = tcur.next()
        for id in idList:
            ad = acur.get(id)
            outputList.append(ad)
        termsBase.close()
        adBase.close()
        return print(outputList) ####
    else:
        termBase.close()
        adBase.close()
        return outputList

inp = ['camera']
termSearch(inp)