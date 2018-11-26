import re
import xml.etree.ElementTree as ET
import queries as q
outputBrief = True

def mainMenu():
    global outputBrief
    print('Output Type: Brief' if outputBrief else 'Output Type: Full')
    print('Type a proper search query')
    print('Type output=brief or output=full to change output type')
    print('Or type !exit to exit')
    res=input()

    if res.startswith('output=') or res.startswith('output ='):
        outputType=re.split(r'=', res.replace(' ', ''))

        if outputType[1].lower() == 'full':
            outputBrief = False
            print('')
            mainMenu()
        elif outputType[1].lower() == 'brief':
            outputBrief = True
            print('')
            mainMenu()
        else:
            print('\nInvalid Input type')
            mainMenu()
    
    elif res == '!exit':
        print('\nGoodbye')
        exit()
    
    elif res:
        results = q.userQueries(parser(inputParser(res)))
        for ad in results:
            queryPrinter(ad)
    else:
        print('\nInvalid Input')
        mainMenu()

def inputParser(res):
    #splits and groups them to remove spaces
    res = res.split()
    i=0
    data=[]
    while i < len(res):
        #if it's the last term
        if i == len(res)-1:
            data.append(res[i])     
            i+=1
            continue

        #word doesn't contain <=> characters
        if not re.search(r'[<=>]+', res[i]):
            #peek if next item starts with a symbol
            if re.match(r'^[<=>]+', res[i+1]):
                #if it's only symbol
                if re.fullmatch(r'[<=>]+', res[i+1]):
                    data.append(res[i] + res[i+1] + res[i+2])
                    i+=3
                    continue
                
                #if it has words
                elif re.search(r'[\w]+',res[i+1]):
                    data.append(res[i] + res[i+1])
                    i+=2
                    continue
            
        #if res ends with a symbol
        elif re.search(r'[<=>]+$', res[i]):
            data.append(res[i] + res[i+1])
            i+=2
            continue
            
        data.append(res[i])     
        i+=1

    return data

def parser(data):
    #parsing after spaces are removed
    queries=[]
    for query in data:
        #if they have sympbols
        if re.search(r'[<=>]+', query):
            queries.append(re.split(r'([<=>]+)', query))
             
        #if they have %
        elif re.search(r'[%]+$', query):
            l=re.split(r'([%]+)$', query)
            l.pop()
            queries.append(l)
        
        else:
            queries.append([query])

    return queries

def queryPrinter(query):
    global outputBrief
    adQuery = ET.fromstring(query[1])

    if outputBrief:
        print('\nAD ID: ' + query[0])
        print('Title: ' + adQuery[4].text + '\n')
        

    elif not outputBrief:
        print('\nAD ID: ' + query[0])
        print('Date: ' + adQuery[1].text)
        print('Location: ' + adQuery[2].text)
        print('Category: ' + adQuery[3].text)
        print('Title: ' + adQuery[4].text)
        print('Description: ' + adQuery[5].text)
        print('Price: ' + adQuery[6].text + '\n')

    else:
        print('\nSomething Went Wrong')
        mainMenu()


mainMenu()