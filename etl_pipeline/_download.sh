echo "_download has started"
cd $1
mkdir data
cd data
echo "data directory created"
wget $2
echo "data downloaded"
file_name=$(ls)
mv $file_name data.tar.gz
echo "renaming complete"