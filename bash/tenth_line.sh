#!/bin/bash
FILE_NAME="examples/tenth_line.txt"
# cnt = 0
# while read line && [ $cnt -le 10]; do
#   let 'cnt = cnt + 1'
#   if [ $cnt -eq 10]; then
#     echo $line
#     exit 0
#   fi
# done < $FILE_NAME
sed -ne 10p < $FILE_NAME
