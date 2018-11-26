# This function handles each query that the user inputs
# then performs an intersection on all the queries
# if there is more than one
import termSearch as ts
import equalSearch as es
import rangeSearch as rs
from bsddb3 import db

def userQueries(userInput):
    # userInput is assumed to be a list of lists
    # the output of each query function is a list
    idList = []
    ads = []
    adsDB = db.DB()
    adsDB.open('ads.idx', None, db.DB_HASH)
    adsCur = adsDB.cursor()

    if len(userInput) > 0:
        for query in userInput:
            if len(query) == 3:
                if query[1] in ['>','<','<=','=<','>=','=>']:
                    idList.append(rs.rangeSearch(query))
                else:
                    idList.append(es.equalSearch(query))
            else:
                idList.append(ts.termSearch(query))
        # all query results ids are in idList
        # we perform a intersection on list of list if there is more than one query
        if len(idList) > 1:
            sectList = []
            for li in idList:
                tempList = []
                for id in li:
                    tempList.append(id.decode())
                sectList.append(tempList)

            idList = list(set(sectList[0]).intersection(*sectList[1:]))
            for id in idList:
                ad = adsCur.get(id.encode('utf-8'), db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                ads.append([adid,descr])
            adsDB.close()
            return ads
        else:
            for id in idList[0]:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                ads.append([adid,descr])
            adsDB.close()
            return ads
    else:
        print('Something is wrong with user input')
        return

    