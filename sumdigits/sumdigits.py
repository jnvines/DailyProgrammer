#!/usr/bin/python
import sys

def usage():
	print 'This program will take 1 argument and returned the summed'
	print 'value of the digits.'
	print 'Example: ./sumdigits.py 31337 returns 8'

if len(sys.argv)!=2:
	print 'Please pass one and only one number'
	usage()
	exit(1)

s=str(sys.argv[1])

while len(s) > 1:
	summed = 0 
	for i in range(0,len(s)):
		summed+=int(s[i])
	s = str(summed)

print 'The sum is ' + str(s)
