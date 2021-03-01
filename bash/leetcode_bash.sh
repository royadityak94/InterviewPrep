#!/bin/sh

##----------------------------------------------------------##
#	Print 10th line of a file
##----------------------------------------------------------##
contents=`sed -ne '10p' 'examples/tenth_line.txt'`
#echo "File Contents = " $contents
printf "File Contents = %s\n" "$contents";

##----------------------------------------------------------##
#	Vaid Phone Number
#	(xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
##----------------------------------------------------------##
matched=` grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' examples/phone_number.txt | tr ':' ' ' `

echo "All matched contents = " "${matched_arr}"

# for phone_no in "${matched[@]}" 
# do
# 	printf "Phone: %s\n" $phone_no 
# done


##----------------------------------------------------------##
#	Transpose File Contents
#	Rows -> Columns, Columns -> Rows
##----------------------------------------------------------##
awk '{
	for (i=1; i <= NF; i++){
		if (NR == 1){
			s[i] = $i;
		} else {
			s[i] = s[i] " " $i;
		}
	}
}
END {
	for (i=1; s[i] != ""; i++) {
		print s[i];
	}
}' 'examples/transpose_file.txt'

##----------------------------------------------------------##
#	Word Counter
#	the 4, is 3, sunny 2, day 1
##----------------------------------------------------------##
echo "Initiating word counter ..."
FILE_NAME='examples/word_count.txt'
cat $FILE_NAME | tr -s [:blank:] '\n' | tr -d [:punct:] | sort | uniq -c | sort -nr -k 1 | awk '{ print $2, $1}' > 'examples/output_word_count.txt'