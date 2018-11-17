import sys
import re
import xml.etree.ElementTree as ET

fileName = open(str(sys.argv[1]),'r')

fileData = [line.rstrip('\n') for line in fileName]

for line in fileData:
    if line.startswith('<ad>'):
        lineData = ET.fromstring(line)


        stripTi = ""
        for ch in lineData[4].text:
            if re.match(r'([0-9a-zA-Z_-])+', ch):
                stripTi += ch
            else:
                stripTi += ' '

        stripTerms = ""
        for ch in lineData[5].text:
            if re.match(r'([0-9a-zA-Z_-])+', ch):
                stripTerms += ch
            else:
                stripTerms += ' '

        termsData = stripTi.split()
        termsData.extend(stripTerms.split())
        terms=[]
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
