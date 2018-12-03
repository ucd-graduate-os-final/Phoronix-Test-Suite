#!/bin/sh

cd /root/pts_project/

python3 Scripts/pts-demo.py vm_test 1 run

git add -A
git commit -m "Changed code"
git pull
git push
git pull
