#!/usr/bin/python2
import sys
import code as code
import re

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
elif(len(sys.argv)==11):
#	print sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
	FIRST='1'
	FOLLOW='1'
	CLOSURE='1'
	PARSE_TABLE='1'
	ACTION_TABLE='1'
	expression=str(sys.argv[6])
	LRCLOSURE='1'
	LRACTION_TABLE='1'
	expression1=str(sys.argv[9])
	LACLOSURE='1'
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
