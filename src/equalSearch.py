# search for direct equalities
# assumes that the input expression is list of length 3
from bsddb3 import db

# expres[0] == price,date,location
# expres[1] == '='
# expres[2] == term to search for
def equalSearch(expres):
    outputList = []
    idList = []
    searchType = expres[0]
    
    if searchType == 'price':
        priceBase = db.DB()
        priceBase.open('prices.idx', None, db.DB_BTREE)
        pcur = priceBase.cursor()
        
        adBase = db.DB()
        adBase.open('ads.idx', None, db.DB_HASH)
        acur = adBase.cursor()
        # expres[2] is the value that is searched in the equality
        value = expres[2].encode('utf-8')
        iter = pcur.get(value, db.DB_SET)
        while iter:
            if iter[0] == value:
                record = iter[1].decode().split(',')
                #record[0] is the ad id
                idList.append(record[0].encode('utf-8'))
            iter = pcur.next_dup()
        for id in idList:
            ad = acur.get(id, db.DB_SET)
            adid = ad[0].decode()
            descr = ad[1].decode()
            outputList.append([adid,descr])
        priceBase.close()
        adBase.close()
        return print(outputList)

    elif searchType == 'date':
        dateBase = db.DB()
        dateBase.open('pdates.idx', None, db.DB_BTREE)
        dcur = dateBase.cursor()

        adBase = db.DB()
        adBase.open('ads.idx', None, db.DB_HASH)
        acur = adBase.cursor()

        value = expres[2].encode('utf-8')
        iter = dcur.get(value, db.DB_SET)
        while iter:
            if iter[0] == value:
                record = iter[1].decode().split(',')
                idList.append(record[0].encode('utf-8'))
            iter = dcur.next_dup()
        for id in idList:
            ad = acur.get(id, db.DB_SET)
            adid = ad[0].decode()
            descr = ad[1].decode()
            outputList.append([adid,descr])
        dateBase.close()
        adBase.close()
        return print(outputList)
    
    elif searchType == 'cat':
        dateBase = db.DB()
        dateBase.open('pdates.idx', None, db.DB_BTREE)
        dcur = dateBase.cursor()

        adBase = db.DB()
        adBase.open('ads.idx', None, db.DB_HASH)
        acur = adBase.cursor()
        #category that is searched needs to be case insensitive
        #category is an exact match
        category = expres[2].lower()
        iter = dcur.first()
        while iter:
            record = iter[1].decode().split(',')
            #record[0] = ad id, record[1] = category, record[2] = location
            if record[1] == category:
                idList.append(record[0].encode('utf-8'))
            iter = dcur.next()
        for id in idList:
            ad = acur.get(id, db.DB_SET)
            adid = ad[0].decode()
            descr = ad[1].decode()
            outputList.append([adid,descr])
        dateBase.close()
        adBase.close()
        return outputList

    else:
        return
