#!/bin/bash
#Author: Nick Vines
#Email: jnvines@gmail.com
#Date: June 12, 2013


usage()
{
cat << EOF
usage: $0 NUMBER

This script will sum the digits of of a single number. The formal problem description is found at the below url.
http://www.reddit.com/r/dailyprogrammer/comments/1cundw/042213_challenge_123_easy_sum_them_digits/

The program is called with one argument, a single positive integer. The program will output the sum of its digits.

Example: ./sumdigits.sh 31337
Output: 8 

EOF
}

NUMBER=$1

if [ -z "$NUMBER" ] 
then
	echo "Please give me a number"
	usage
	exit 1
fi

if [ -n "$2" ]
then
	echo "Please only give me one argument"
	usage
	exit 1
fi

s="$NUMBER"

while [ ${#s} -gt  1 ]; do
	SUMMED=0	
	for i in $(seq 0 $((${#s}-1))); do
#		echo "s[$i] = \"${s:$i:1}\""
		SUMMED=$((SUMMED + ${s:$i:1}))
	done
#	echo "Summed is $SUMMED"
	s="$SUMMED"
done

echo "The summed digits is $s"
