##!/usr/bin/env bash
FILE_NAME='examples/word_count.txt'
cat $FILE_NAME | tr -s [:blank:] '\n' | tr -d [:punct:] | sort | uniq -c | sort -nr -k 1 | awk '{ print $2, $1 }'
