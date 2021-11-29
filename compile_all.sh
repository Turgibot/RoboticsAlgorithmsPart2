#!/bin/sh
echo Compiling all manim animation and uploading to website

manim chapter5.py Chap5_00


echo uploading to github

cd ..
git add .
git commit -m "uploading from script"
git push