cd /root/data/dogNcat/dogNcat_photos/dogs



for i in $(ls |grep \.jpeg); do
  convert $i $(echo "$i" |cut -d'.' -f1).jpg
done

#png covert to jpg
for i in $(ls |grep \.png); do
 convert $i $(echo "$i" |cut -d'.' -f1).jpg
done

#ashx covert to jpg
for i in $(ls |grep \.ashx); do
  convert $i $(echo "$i" |cut -d'.' -f1).jpg
done

mkdir /root/data/dogNcat/dogNcat_photos/dog

cp /root/data/dogNcat/dogNcat_photos/dogs/*.jpg  /root/data/dogNcat/dogNcat_photos/dog/

cd /root/data/dogNcat/dogNcat_photos
rm -r dogs
cd /root/data/dogNcat/dogNcat_photos/dog/

for i in $(ls |grep \.jpg); do
  convert $i -resize 400x400 -quality 100 $i
done


cd /root/data/dogNcat/dogNcat_photos/cats

#jpeg covert to jpg
for i in $(ls |grep \.jpeg); do
  convert $i $(echo "$i" |cut -d'.' -f1).jpg
done

#png covert to jpg
for i in $(ls |grep \.png); do
  convert $i $(echo "$i" |cut -d'.' -f1).jpg
done

#ashx covert to jpg
for i in $(ls |grep \.ashx); do
  convert $i $(echo "$i" |cut -d'.' -f1).jpg
done


mkdir /root/data/dogNcat/dogNcat_photos/cat

cp /root/data/dogNcat/dogNcat_photos/cats/*.jpg /root/data/dogNcat/dogNcat_photos/cat/

cd /root/data/dogNcat/dogNcat_photos
rm -r cats
cd /root/data/dogNcat/dogNcat_photos/cat/

for i in $(ls |grep \.jpg); do
  convert $i -resize 400x400 -quality 100 $i
done
 
