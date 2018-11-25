# search for direct equalities
# assumes that the input expression is list of length 3
# express[0] == price,date,location
# express[1] == '='
# express[2] == term to search for


def equalSearch(express):
    outputList = []
    idList = []
    key = express[0].decode()
    
    if key == 'price':
        priceDb = db.DB()
        priceDB.open('price.idx')
        cur = priceDb.cursor()
        iter = cur.first()
        while iter:
            



    elif key == 'pdate':
        dateDB = db.DB()
        dateDB.open('pdate.idx')


    elif key == 'cat':
        dateDB = db.DB()
        dateDB.open('pdate.idx')


    else:
        return
    
    