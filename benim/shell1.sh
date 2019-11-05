#!/bin/bash
file=/home/dyilmaz/Desktop/book/benim/all
cp deneme $file
cd $file
split -l 9 deneme
cd $file
rm deneme
ls | while read filename
do
  tr '\n' '*'< $(echo $filename) > 1$(echo $filename)
done
#rm x*
#paste -s * > last.csv
#rm 1*
#cd /home/dolmussaatleri/book/all
#sed -i '1d;$d' last.csv
