import sys
import re
import xml.etree.ElementTree as ET

fileName = open(str(sys.argv[1]),'r')

fileData = [line.rstrip('\n') for line in fileName]

for line in fileData:
    #parses each line then formats them to lists
    if line.startswith('<ad>'):
        lineData = ET.fromstring(line)
        
        #terms parsing
        #splits all words that are allowed and removes unneeded characters
        terms = (lineData[4].text or '') + ' ' +  (lineData[5].text or '')
        terms = re.findall(r"([a-zA-Z0-9-_]+)", terms)

        with open('terms.txt', 'a') as termsFile:
            for word in terms:
                if len(word) > 2:
                    termsFile.write(':'.join([word.lower(),lineData[0].text]) + '\n')
        
        #pdates parsing
        if lineData[1].text:
            pdate = ':'.join([lineData[1].text,lineData[0].text]) + ',' + lineData[3].text + ',' + lineData[2].text
            
            with open('pdates.txt', 'a') as pdateFile:
                pdateFile.write(pdate + '\n')
        
        #prices parcing
        if lineData[6].text:
            #add the digits backwards into a string of spaces
            prices = '           '
            for i in lineData[6].text[::-1]:
                head, middle, tail = prices.rpartition(' ')
                prices = head + i + tail
            
            prices = ':'.join([prices,lineData[0].text]) + ',' + lineData[3].text + ',' + lineData[2].text
            
            with open('prices.txt', 'a') as pricesFile:
                pricesFile.write(prices + '\n')

        #ads parsing
        ads = ':'.join([lineData[0].text,line])
        with open('ads.txt', 'a') as adsFile:
            adsFile.write(ads + '\n')
