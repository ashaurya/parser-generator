#!/usr/bin/python2
import sys
import code as code

if(len(sys.argv)==1):
	while True:
		try:
#			s = raw_input('yacc > ')
			s = raw_input()
		except EOFError:
			break
		if not s: 
			continue
		if(s=='$'):
			break
		result = code.parser.parse(s)

		
#else:
#	if(sys.argv[1]=='-help' or sys.argv[1]=='--help'):
#		try:
#			f = open('help.txt', 'r')
#			for line in f:
#				print line
#		except IOError:
#			print "Error opening help file"		
#	else:
#		if(len(sys.argv)==4 and (sys.argv[2]=='-start' or sys.argv[2]=='--start')):
#			code.firstnt.append(sys.argv[3])
#		try:
#			f = open(sys.argv[1], 'r')
#			for line in f:
#				if(line=='$'):
#					break
#				result = code.parser.parse(line)
#		except IOError:
#			print "Error reading file"
