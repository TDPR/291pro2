import subprocess as sp
import os

# Unix command sort -u <filename> sorts the file and removes duplicates
sp.call(['sort','-u','terms.txt','-o','terms.txt'])
sp.call(['sort','-u','pdates.txt','-o','pdates.txt'])
sp.call(['sort','-u','prices.txt','-o','prices.txt'])
sp.call(['sort','-u','ads.txt','-o','ads.txt'])

#setting up each file for db_load, such that / are gone, key and data alternate lines
filenames = ['terms.txt', 'pdates.txt','prices.txt','ads.txt']
for name in filenames:
    temp = open('temp.txt','w+')
    fo = open(name,'r')
    for line in fo:
        sline = line.split(':')
        if name == 'prices.txt':
            temp.write(str(int(sline[0]))+'\n')
        else:
            temp.write(sline[0]+'\n')
        temp.write(sline[1])
    fo.close()
    temp.close()
    os.rename('temp.txt', name)

# now using db_load for each file, assumes that Berkely db is installed
sp.call(['db_load','-c','duplicates=1','-f','terms.txt','-T','-t','btree','terms.idx'])
sp.call(['db_load','-c','duplicates=1','-f','pdates.txt','-T','-t','btree','pdates.idx'])
sp.call(['db_load','-c','duplicates=1','-f','prices.txt','-T','-t','btree','prices.idx'])
sp.call(['db_load','-f','ads.txt','-T','-t','hash','ads.idx'])
