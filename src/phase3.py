import re

def mainMenu():
    print('Type a proper search query')
    print('Or type !exit to exit')
    res=input()

    if res:
        parser(res)

    elif res == '!exit':
        print('\nGoodbye')
        exit()
    else:
        print('\nInvalid Input')
        mainMenu()

def parser(res):
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

    print(data)

mainMenu()