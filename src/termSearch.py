# takes input of a list of length 1, or length 2 if modulo

import re
from bsddb3 import db

def termSearch(keyword):
    #open the data bases we will use
    # working lists
    idList = []

    # index 0 is reserved for the keyword
    # index 1 is reserved for modulo, if it exists
    if len(keyword) == 1:
        termsBase = db.DB()
        termsBase.open('terms.idx', None, db.DB_BTREE)
        tcur = termsBase.cursor()

        adBase = db.DB()
        adBase.open('ads.idx', None, db.DB_HASH)
        acur = adBase.cursor()
        keyword[0] = keyword[0].lower().encode('utf-8') #necessary to match the db

        iter = tcur.get(keyword[0], db.DB_SET)
        while iter:
            if iter[0] == keyword[0]:
                idList.append(iter[1])
            iter = tcur.next_dup()
        termsBase.close()
        return idList
    
    elif len(keyword) == 2:
        termsBase = db.DB()
        termsBase.open('terms.idx', None, db.DB_BTREE)
        tcur = termsBase.cursor()
        
        adBase = db.DB()
        adBase.open('ads.idx', None, db.DB_HASH)
        acur = adBase.cursor()

        bitKeyword = keyword[0].encode('utf-8')
        iter = tcur.set_range(bitKeyword)
        while iter:
            # iter[0] is the key
            if bitKeyword in iter[0]:
                idList.append(iter[1])
            iter = tcur.next()
        termsBase.close()
        return idList
    else:
        termBase.close()
        return idList
