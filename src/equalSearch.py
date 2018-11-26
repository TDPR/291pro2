# search for direct equalities
# assumes that the input expression is list of length 3
from bsddb3 import db

# expres[0] == price,date,location
# expres[1] == '='
# expres[2] == term to search for
def equalSearch(expres):
    idList = []
    searchType = expres[0]
    
    if searchType == 'price':
        priceBase = db.DB()
        priceBase.open('prices.idx', None, db.DB_BTREE)
        pcur = priceBase.cursor()
        # expres[2] is the value that is searched in the equality
        
        #dealing with the whitespce in berkeley db
        value = expres[2]
        nchar = 11
        offset = nchar - len(value)
        value = ' '*offset + value
        value = value.encode('utf-8')

        iter = pcur.get(value, db.DB_SET)
        while iter:
            if iter[0] == value:
                record = iter[1].decode().split(',')
                #record[0] is the ad id
                idList.append(record[0].encode('utf-8'))
            iter = pcur.next_dup()
        priceBase.close()
        return idList

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
        dateBase.close()
        return idList
    
    elif searchType == 'cat':
        dateBase = db.DB()
        dateBase.open('pdates.idx', None, db.DB_BTREE)
        dcur = dateBase.cursor()

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
        dateBase.close()
        return idList
    elif searchType == 'location':
        dateBase = db.DB()
        dateBase.open('pdates.idx', None, db.DB_BTREE)
        dcur = dateBase.cursor()

        adBase = db.DB()
        adBase.open('ads.idx', None, db.DB_HASH)
        acur = adBase.cursor()
        #category that is searched needs to be case insensitive
        #category is an exact match
        location = expres[2].lower()
        iter = dcur.first()
        while iter:
            record = iter[1].decode().split(',')
            #record[0] = ad id, record[1] = category, record[2] = location
            if record[2].lower() == location:
                idList.append(record[0].encode('utf-8'))
            iter = dcur.next()
        dateBase.close()
        return idList

    else:
        return
