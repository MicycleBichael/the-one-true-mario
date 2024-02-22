#!/usr/local/bin/bash
echo "Testing..."
chmod u+x bashtest.sh

for i in {1..4}
do 
    python3 train.py
done
for i in {1..9}
do
    python3 train.py --test_type "positive"
done