#!/usr/bin/python
import sys
import re

def usage():
	print 'This program will take one and only one argument, the path to the file to analyze'

def simple_analytics(file):
	word_count=0
	symbol_count=0
	letter_count=0
	re_word=re.compile("[a-zA-Z]+")
	re_sym=re.compile("[^a-zA-Z\s]+")
	re_letters=re.compile("[a-zA-Z]")
	for x in file:
		x = x.rstrip()
		if len(x) == 0:
			continue
		word_count+=(len(re_word.findall(x)))
		symbol_count+=(len(re_sym.findall(x)))
		letter_count+=(len(re_letters.findall(x)))
		#print 'Length of this line is ' + str(len(x.rstrip())) + ' with ' + str(word_count) + ' words and ' + str(letter_count) +' letters'	+ \
		#	' and ' + str(symbol_count) + ' symbols'
		#word
		#count words, symbols, and letters...
	print str(word_count) + " words"
	print str(symbol_count) + " symbols"
	print str(letter_count) + " letters"
	
	
def common(file, delim, top):
	#returns the top top entries from the file separated by delim. 
	#example, common(f,' ',3) will return the top 3 words (whitespace delim)
	#example, common(f,'',3) will return the top 3 letters
	#note, delim = '' will ignore whitespace
	#note, this will always ignore newlines
	exit(0)

def paragraph_start(file,top):
	#returns the top top starting words of the paragraphs in file file
	#paragraph is surrounded by beginning of file, end of file, or empty line
	exit(0)

def occurence(file,  occurence):
	#returns the words occuring occurence in file file. 
	#word is a-zA-Z surrounded by whitespace, newline, or beginning/end of file
	exit(0)

def letters_missing(file):
	#returns the list of letters not in the file. 
	exit(0)

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
