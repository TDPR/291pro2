# load the db files
import subprocess as sp
# now using db_load for each file, assumes that Berkely db is installed
sp.call(['db_load','-f','Tterms.txt','-T','-t','btree','terms.idx'])
sp.call(['db_load','-f','Tpdates.txt','-T','-t','btree','pdates.idx'])
sp.call(['db_load','-f','Tprices.txt','-T','-t','btree','prices.idx'])
sp.call(['db_load','-f','Tads.txt','-T','-t','hash','ads.idx'])