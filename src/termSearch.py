# takes input of a list of length 1, or length 2 if modulo

def termSearch(keyword):
    #open the data bases we will use
    termsBase = db.DB()
    termsBase.open('terms.idx')
    adBase = db.DB()
    adBase.open('ads.idx')

    # working lists
    outputList = []
    idList = []
    
    # index 0 is reserved for the keyword
    # index 1 is reserved for modulo, if it exists
    if len(keyword) == 1:
        keyword[0] = keyword[0].encode('utf-8') #necessary to match the db
        iter = tcur.first()
        while iter:
            if iter[0] == keyword[0]:
                idList.append(iter[1])
            iter = cur.next()
        for id in idList:
            ad = cur.get(id)
            outputList.append(ad)
        termBase.close()
        adBase.close()
        return outputList
    
    elif len(keyword) == 2:
        iter =cur.first()
        while iter:
            key = iter[0].decode()
            if re.search(keyword, key):
                idList.append(iter[1])
            iter = cur.next()
        for id in idList:
            ad = cur.get(id)
            outputList.append(ad)
        termBase.close()
        adBase.close()
        return outputList
    else:
        termBase.close()
        adBase.close()
        return outputList

            