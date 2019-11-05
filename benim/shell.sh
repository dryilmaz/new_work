#!/bin/bash
cp deneme /home/dyilmaz/Desktop/book/benim/all
cd /home/dyilmaz/Desktop/book/benim/all
sed -i 's~https://imageserver.kitapyurdu.com/select.php?imageid=0&width=500&isWatermarked=true~https://herokitap.com/select.jpg~g' deneme
split -l 9 deneme
cd /home/dyilmaz/Desktop/book/benim/all
rm deneme
ls | while read filename
do
  tr '\n' '*'< $(echo $filename) > 1$(echo $filename)
done
rm x*
paste -s * > last.csv
rm 1*
