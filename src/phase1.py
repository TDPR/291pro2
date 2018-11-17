import sys
import re
import xml.etree.ElementTree as ET

fileName = open(str(sys.argv[1]),'r')

fileData = [line.rstrip('\n') for line in fileName]

for line in fileData:
    if line.startswith('<ad>'):
        lineData = ET.fromstring(line)

        termsData = lineData[4].text + lineData[5].text

        #splits all words that are allowed and removes unneeded characters
        termsData = re.findall(r"([a-zA-Z0-9-_]+)", termsData)
        terms =[]

        for word in termsData:
            if len(word) > 2:
                terms.append(':'.join([word.lower(),lineData[0].text]))

        print(terms)

        pdate = [lineData[1].text, lineData[0].text, lineData[3].text, lineData[2].text]
        print(pdate)
        prices = [':'.join([lineData[6].text,lineData[0].text]), lineData[3].text, lineData[2].text]
        print(prices)
        ads = [':'.join([lineData[0].text,line])]
        print(ads)

        print('\n')
