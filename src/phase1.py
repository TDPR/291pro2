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
        termsData = lineData[4].text + lineData[5].text
        
        #splits all words that are allowed and removes unneeded characters
        termsData = re.findall(r"([a-zA-Z0-9-_]+)", termsData)
        terms =[]

        for word in termsData:
            if len(word) > 2:
                terms.append(':'.join([word.lower(),lineData[0].text]))

        with open('terms.txt', 'a') as termsFile:
            for word in terms:
                termsFile.write(word + '\n')
        
        #pdates parsing
        if lineData[1].text:
            pdate = ':'.join([lineData[1].text,lineData[0].text]) + ',' + lineData[3].text + ',' + lineData[2].text
            
            with open('pdates.txt', 'a') as pdateFile:
                pdateFile.write(pdate + '\n')
        
        #prices parcing
        if lineData[6].text:
            prices = ':'.join([lineData[6].text,lineData[0].text]) + ',' + lineData[3].text + ',' + lineData[2].text
            
            with open('prices.txt', 'a') as pricesFile:
                pricesFile.write(prices + '\n')

        #ads parsing
        ads = ':'.join([lineData[0].text,line])
        with open('ads.txt', 'a') as adsFile:
            adsFile.write(ads + '\n')
