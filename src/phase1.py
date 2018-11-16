import sys
import re

fileName = open(str(sys.argv[1]),'r')

fileData = [line.rstrip('\n') for line in fileName]

for line in fileData:
    if line.startswith('<ad>'):
        print(line+'\n')
