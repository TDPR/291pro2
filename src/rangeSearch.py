from bsddb3 import db
import sys
import re



def rangeSearch(query):
    #query entering range check will have a len == 3 and will be broken into
    #three sections: file key (eg. date, price), operator (eg. <, >), and value (eg. 20, 2018/04/02)
    key = query[0]
    operator = query[1]
    value = query[2]
    adID = []

    if key == 'date':
        pdatesDB = db.DB()
        pdatesDB.open('pdates.idx', None, db.DB_BTREE)
        pdatesCur = pdatesDB.cursor()
        dDupCur = pdatesDB.cursor()

        if operator == '>=' or operator == '=>':
            #start at the beginning of index (min) and appends to list
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()
            pdatesDB.close()
            return adID
                   
        if operator == '>':
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()  
            pdatesDB.close()
            return adID

        elif operator == '<=' or operator == '=<':
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()
            pdatesDB.close()
            return adID

        elif operator == '<':
            itr = pdatesCur.get(value.encode('utf-8'), db.DB_SET)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = pdatesCur.next()
            pdatesDB.close()
            return adID

    if key == 'price':
        priceDB = db.DB()
        priceDB.open('prices.idx', None, db.DB_BTREE)
        priceCur = priceDB.cursor()
        
        nchar = 11
        offset = nchar - len(value)
        value = ' ' * offset + value

        if operator == '>=' or operator == '=>':
            #start at the beginning of index (min) and appends to list
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') == value or itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.next()
            priceDB.close()
            return adID
                    
        if operator == '>':
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            while(itr):
                if itr[0].decode('utf-8') > value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.next()  
            priceDB.close()
            return adID

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
            priceDB.close()
            return adID

        elif operator == '<':
            itr = priceCur.get(value.encode('utf-8'), db.DB_SET_RANGE)
            #goes through any duplicates and appends them to the list
            itr = priceCur.prev()  
            while(itr):
                if itr[0].decode('utf-8') < value:
                    records = itr[1].decode('utf-8').split(',')
                    adID.append(records[0].encode('utf-8'))
                itr = priceCur.prev()
            priceDB.close()
            return adID

    else:
        print('Cannot perform any range searches. Please try again')
        return

