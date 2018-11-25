import subprocess as sp
import os

# Unix command sort -u <filename> sorts the file and removes duplicates
sp.call(['sort','-u','terms.txt'])
sp.call(['sort','-u','pdates.txt'])
sp.call(['sort','-u','prices.txt'])
sp.call(['sort','-u','ads.txt'])

#setting up each file for db_load, such that / are gone, key and data alternate lines
filenames = ['terms.txt', 'pdates.txt','prices.txt','ads.txt']
for name in filenames:
    temp = open('temp.txt','w+')
    fo = open(name,'r')
    for line in fo:
        sline = line.split(':')
        temp.write(sline[0]+'\n')
        temp.write(sline[1])
    fo.close()
    temp.close()
    Tname = 'T'+ name
    os.rename('temp.txt', Tname)

# now using db_load for each file, assumes that Berkely db is installed
sp.call(['db_load','-f','Tterms.txt','-T','-t','btree','terms.idx'])
sp.call(['db_load','-f','Tpdates.txt','-T','-t','btree','pdates.idx'])
sp.call(['db_load','-f','Tprices.txt','-T','-t','btree','prices.idx'])
sp.call(['db_load','-f','Tads.txt','-T','-t','hash','ads.idx'])