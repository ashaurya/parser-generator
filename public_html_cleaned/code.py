#!/usr/bin/python2
import ply.lex as lex
import ply.yacc as yacc


## ------------- REGEXPs ------------------------------------------------

tokens = (
    'SCOLON',
    'INT',
    'STRING',
    'ID',
    'CHAR',
    'PIPE',
    'DPREC',
    'PREC',
    'MERGE',
    'COLON',
    'TYPE'
)

t_CHAR                         = r'\'.\''
t_ID                               = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PIPE                           = r'\|'
t_SCOLON                    = r';'
t_COLON                      = r':'
t_DPREC                       =r'%dprec'
t_PREC                          =r'%prec'
t_MERGE                      =r'%merge'
t_TYPE                          =r'<[^\0\n>][^\0\n>]*>'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'L?\"(\\.|[^\\"])*\"'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
#    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

rules = []
terminals = set()
nonterms = set()
firstnt = []

def findRule(p_p):
	if(rules==[]):
		if(len(firstnt)==0):
			firstnt.append(p_p[0])
#			print 'firstnt :', firstnt					#firstnt stores the first non terminal!
		return 0
	else:
		for a in range(0, len(rules)):
			if(rules[a]==p_p):
				return 1
		else:
			return 0
		
def funcRule(p_):
	global rules
	if(findRule(p_)==0):
		ls = [p_[0]]
		for a in range(1, len(p_)):
			if(len(p_[a])==1):
				ls.extend(p_[a])
			else:
				ls.append(p_[a])
		if(len(rules)==0):
			rules = [ls]
		else:
			rules.append(ls)
			
## ------------- GRAMMAR ------------------------------------------------
def p_grammer(p):
    '''grammar	: rules 
                | grammar rules'''

def p_rules(p):
	'rules : id_colon rhses_1'
	lst = [p[1]]
	i=0
	while(i<len(p[2])):
		if(p[2][i]=='|'):
			funcRule(lst)
			lst = [p[1]]
		else:
			if(len(p[2][i])==1):
				lst.extend(p[2][i])
			else:
				try:
					lst = lst+(p[2][i])
				except TypeError:
					lst.append(p[2][i])
		i = i+1
	funcRule(lst)
		

def p_rhses_1_pipe(p):
	'rhses_1	:  rhses_1 PIPE rhs'
	lst = []
	lst = lst+(p[1])
	lst.extend('|')
	if(p[3]==[' ']):
		terminals.add(' ')
		lst.append(p[3])
	else:
		lst = lst + (p[3])
	p[0] = lst
	
def p_rhses_1_scolon(p):
	'rhses_1	:  rhses_1 SCOLON'
	p[0] = p[1]
	
def p_rhses_1(p):
	'rhses_1	: rhs'
	p[0] = p[1]
	if(p[1]==[' ']):
		terminals.add(' ')
	
def p_rhs_prec(p):
	'rhs	: rhs PREC symbol'
	lst = p[1]
	lst.append(p[3])
	p[0] = lst
	
def p_rhs(p):
	'rhs	: rhs symbol'
	if(p[1]==[' ']):
		lst = [p[2]]
	else:
		lst = p[1]
		lst.append(p[2])
	
	p[0] = lst
#	print "Random ter %r ", p[0]               #Random p[0] printing

	for a in p[0]:
		if(a in nonterms):
			continue
		else:
			terminals.add(a)
	
def p_rhs_drec(p):
	'rhs	: rhs DPREC INT'
	lst = p[1]
	lst.append(p[3])
	p[0] = lst
	
def p_rhs_merge(p):
	'rhs	: rhs MERGE TYPE'
	lst = p[1]
	lst.append(p[3])
	p[0] = lst
	
def p_rhs_null(p):
	'rhs	: '
	p[0] = [' ']

def p_id_char(p):
	'id : CHAR'
	p[0] = p[1]
	
def p_id(p):
	'id : ID'  
	p[0] = p[1] 
	
def p_id_colon(p):
	'id_colon	: ID COLON'
	p[0] = p[1]
	if(p[1] in terminals):
		terminals.remove(p[1])
	nonterms.add(p[1])

def p_symbol(p):
	'symbol	: string_as_id'
	p[0] = p[1]
	if(p[1] in nonterms):
		pass
	else:
		terminals.add(p[1])
	
def p_symbol_id(p):
	'symbol	: id'
	p[0] = p[1]
	if(p[1] in nonterms):
		pass
	else:
		terminals.add(p[1])
		
def p_string_as_id(p):
	'string_as_id	: STRING'
	p[0] = p[1]
	
lexer = lex.lex()

def p_error(p):
    print "Syntax error in input!"

parser = yacc.yacc()
