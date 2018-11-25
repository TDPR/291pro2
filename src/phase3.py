import re
import xml.etree.ElementTree as ET
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
        parser(inputParser(res))   

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

    print(queries)

def queryPrinter(query):
    global outputBrief
    
    #TODO REMOVE
    query = ['1304786670', '<ad><aid>1304786670</aid><date>2018/11/07</date><loc>Calgary</loc><cat>cam5era-camcorder-lens</cat><ti>Nikon 500 mm F4 VR</ti><desc>I have owned this Nikon lens for about 2 years and purchased it new in Calgary. The lens is extremely sharp, and fast focusing. It is a wildlife or bird photographers dream lens. I am selling it</desc><price>8500</price></ad>']
    
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