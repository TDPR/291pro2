import re
outputBrief = True

def mainMenu():
    print('Type a proper search query')
    print('Type output=brief or output=full to change output type')
    print('Or type !exit to exit')
    res=input()

    if res.startswith('output=') or res.startswith('output ='):
        print('Hello')
    
    elif res:
        parser(inputParser(res))   

    elif res == '!exit':
        print('\nGoodbye')
        exit()
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


mainMenu()