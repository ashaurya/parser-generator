#!/usr/bin/python2
import code as code
import handler as h

def calc_closure(item):
	closure = []
	closure.append(item)
	change = 1
	while(change==1):
		change = 0
		for _item_ in closure:
			place = int(_item_[len(_item_)-1])
			if(place >= len(_item_)-1 or place==0):
				break
			else:
				if(_item_[place] in code.nonterms):
					for a in code.rules:
						if(_item_[place]==a[0]):
							temp = []
							temp.extend(a)
							temp.extend('1')
							for a in range(0, len(closure)):
								if(temp==closure[a]):
									break
							else:
								closure.append(temp)
								change= 1
				else:
					break
	return closure

for rule_no in range(0, len(code.rules)):
	item_ = []
	item_.extend(code.rules[rule_no])
	item_.extend('0')
	for a in range(1, len(item_)-1):
		place = a #position of dot
		item_[len(item_)-1] = str(place)
		closure_set = calc_closure(item_)
		#print closure_set

#closure complete		
#goto calculations
for a in code.firstnt:	
	b = a+'prime'
#	print "Kya hai?"
	rule = [b, a]
rule.extend('1')
code.rules.append(rule)

if(h.CLOSURE=='1'):
	print "\n<h1 align=\"center\">Closure Set:</h1><BR>"

I_o = calc_closure(rule)
if(h.CLOSURE=='1'):
	print "\nI_o:<BR>"
for i in range(0, len(I_o)):
	if(h.CLOSURE=='1'):
		print I_o[i], "<BR>"
if(h.CLOSURE=='1'):
	print "\n<BR><BR>"

def calc_goto(set_prod, var):
	set_ret = []
	for rule_no in range(0, len(set_prod)):
		rule = set_prod[rule_no]
		l = len(rule)
		for a in range(1, l-1):
			if(var==rule[a] and a==int(rule[l-1])):
				temp = []
				temp.extend(rule)
				temp[l-1] = str(int(temp[l-1])+1)
				c = calc_closure(temp)
				for b in range(0, len(c)):
					for r in range(0, len(set_ret)):
						if(c[b]==set_ret[r]):
							break
					else:
						set_ret.append(c[b])
	return set_ret
	
for a in code.nonterms:
	I_1 = calc_goto(I_o, a)
	if(h.CLOSURE=='1'):
		print "a = ", a ,"<BR>"
	for i in range(0, len(I_1)):
		if(h.CLOSURE=='1'):
			print I_1[i],"<BR>"
	if(h.CLOSURE=='1'):
		print "\n<BR><BR>"

for a in code.terminals:
	I_1 = calc_goto(I_o, a)
	if(h.CLOSURE=='1'):
		print "a = ", a,"<BR>"
	for i in range(0, len(I_1)):
		if(h.CLOSURE=='1'):
			print I_1[i],"<BR>"
	if(h.CLOSURE=='1'):
		print "\n<BR><BR>"
