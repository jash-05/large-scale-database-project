#!/bin/bash 
# 
# download MESOWEST data description. This is the legend for the 
# data, not the actual data! 
# 
# Note: the legend and data are updated on 15 minute intervals 
 
if [ ! -d ./data ]; then 
mkdir data 
fi 
 
wget -N --no-cache http://mesowest.utah.edu/data/mesowest_csv.tbl.gz 
if [ -f ./mesowest_csv.tbl.gz ]; then 
gunzip mesowest_csv.tbl.gz 
mv mesowest_csv.tbl data/mesowest_csv.tbl.`date "+%Y%m%dT%H%M"` 
fi 