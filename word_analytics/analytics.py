#!/usr/bin/python
import sys

def usage():
	print 'This program will take one and only one argument, the path to the file to analyze'

def simple_analytics(file):
	for x in file:
		x = x.rstrip()
		print 'Length of this line is ' + str(len(x)) 
		#count words, symbols, and letters...
	
def common(file, delim, top):
	#returns the top top entries from the file separated by delim. 
	#example, common(f,' ',3) will return the top 3 words (whitespace delim)
	#example, common(f,'',3) will return the top 3 letters
	#note, delim = '' will ignore whitespace
	#note, this will always ignore newlines

def paragraph_start(file,top):
	#returns the top top starting words of the paragraphs in file file
	#paragraph is surrounded by beginning of file, end of file, or empty line

def occurence(file,  occurence):
	#returns the words occuring occurence in file file. 
	#word is a-zA-Z surrounded by whitespace, newline, or beginning/end of file

def letters_missing(file):
	#returns the list of letters not in the file. 

if len(sys.argv) != 2:
	usage()
	exit(1)


file_to_analyze=sys.argv[1]
print 'We are going to analyze ' + file_to_analyze

try:
	with open(file_to_analyze, 'r') as f: 
		simple_analytics(f)
		#common(f,' ',3)
		#common(f,'',3)
		#paragraph_start(f,3)
		#word_occurence(f,1)

except IOError:
	print 'Error: The following file does not exist: ' + filename
