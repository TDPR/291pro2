#data = [['camera'], ['date','>','2018/11/05'], ['date','<=','2018/11/07'], ['wako', '%'], ['price', '=', 'yipers']]

from bsddb3 import db
import sys
import re



def rangeSearch(query):
    #query entering range check will have a len == 3 and will be broken into
    #three sections: file key (eg. date, price), operator (eg. <, >), and value (eg. 20, 2018/04/02)
    key = query[0]
    operator = query[1]
    value = query[2]
    outputList = []
    adID = []

    if key == 'date':
        pdatesDB = db.DB()
        pdatesDB.open('pdates.idx', None, db.DB_BTREE)
        pdatesCur = pdatesDB.cursor()
        dDupCur = pdatesDB.cursor()
        adsDB = db.DB()
        adsDB.open('ads.idx', None, db.DB_HASH)
        adsCur = adsDB.cursor()

        if operator == '>=' or operator == '=>':
            #start at the beginning of index (min) and appends to list
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                print(itr)
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            pdatesDB.close()
            adsDB.close()
            return outputList
                   
        if operator == '>':
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()  
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            pdatesDB.close()
            adsDB.close()
            return outputList

        elif operator == '<=' or operator == '=<':
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            pdatesDB.close()
            adsDB.close()
            return outputList

        elif operator == '<':
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            pdatesDB.close()
            adsDB.close()
            return outputList

    if key == 'price':
        priceDB = db.DB()
        priceDB.open('prices.idx', None, db.DB_BTREE)
        priceCur = priceDB.cursor()
        adsDB = db.DB()
        adsDB.open('ads.idx', None, db.DB_HASH)
        adsCur = adsDB.cursor()
        
        nchar = 11
        offset = nchar - len(value)
        value = ' ' * offset + value

        if operator == '>=' or operator == '=>':
            #start at the beginning of index (min) and appends to list
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            while(itr):
                print(itr)
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.next()
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            priceDB.close()
            adsDB.close()
            return print(outputList)
                    
        if operator == '>':
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.next()  
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            priceDB.close()
            adsDB.close()
            return print(outputList)

        elif operator == '<=' or operator == '=<':
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            if itr[0] == value.encode('utf-8'):
                while(itr):
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                    itr = priceCur.next_dup()
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            itr = priceCur.prev()    
            while(itr):
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.prev() 
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            priceDB.close()
            adsDB.close()
            return print(outputList)

        elif operator == '<':
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            itr = priceCur.prev()  
            while(itr):
                if itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.prev()
            for id in adID:
                ad = adsCur.get(id, db.DB_SET)
                adid = ad[0].decode()
                descr = ad[1].decode()
                outputList.append([adid,descr])
            priceDB.close()
            adsDB.close()
            return print(outputList)      

    else:
        print('Cannot perform any range searches. Please try again')
        return
 
    


data = ['price','>','50']
rangeSearch(data)


