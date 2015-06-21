#!/usr/bin/python2
import code as code
import handler as h
import run_new as runner

####################### These lines are to be added
for a in code.firstnt:
	b = a+'pRIME'
	rule = [b, a]

code.rules.append(rule)

for r in range(len(code.rules)-1, 0, -1):
  code.rules[r]=code.rules[r-1]
code.rules[0]=rule

for r in range(0,len(code.rules)):
  print code.rules[r]

print
print

code.nonterms.add(b)
nonterm_initial=b
nonterm_initial2=a


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
	rule = [b, a]

rule.extend('1')
code.rules.append(rule)

I_o = calc_closure(rule)
#print "\nI_o:"
#for i in range(0, len(I_o)):
#	print I_o[i]
#print "\n"

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



####################Calculate Goto code, to be replaced
I=[]
I.append([])
I[len(I)-1].append(I_o)
change=True
while change==True:
  change=False
  for I_o in I:
    for a in code.nonterms:
      I_1=calc_goto(I_o[0],a)
      c=False
      if len(I_1)!=0:
	for p in I:
	  if p[0]==I_1:
	    c=True
	if c==False:
	  I.append([])
	  I[len(I)-1].append(I_1)
	  change=True
	  #print I_1
    for a in code.terminals:
      I_1=calc_goto(I_o[0],a)
      c=False
      if len(I_1)!=0:
	for p in I:
	  if p[0]==I_1:
	    c=True
	if c==False:
	  I.append([])
	  I[len(I)-1].append(I_1)
	  #print I_1
	  change=True

#I_o=I[0]
#for a in code.nonterms:
	#I_1 = calc_goto(I_o[0], a)
	#print "GOTO(I_0,"+str(a)+")"
	#for i in range(0, len(I_1)):
		#print I_1[i]
	#if len(I_1)==0:
		#print "Empty"
	#print "\n"
	#original = I_1
	#if len(I_1)!=0:
		#I.append([])
		#I[len(I)-1].append(I_1)

#for a in code.terminals:
	#I_1 = calc_goto(I_o[0], a)
	#print "GOTO(I_0,"+str(a)+")"
	#for i in range(0, len(I_1)):
		#print I_1[i]
	#if len(I_1)==0:
		#print "Empty"
	#print "\n"
	#if len(I_1)!=0:
		#I.append([])
		#I[len(I)-1].append(I_1)

if(h.CLOSURE=='1'):	
	print "<h1 align=\"center\" >Item Sets</h1>"
	m=0	
	for a in I:
		for p in a:
			print "<BR><h2 align=\"center\" >I_%r : </h2>"%m
#			print "<table border=\"3\" align=\"center\">"
			for x in p:
#				print "<tr><td width=\"300\">"
				for l in x:
					print l
					print "<BR>HELLO<BR>"
#				print "</td></tr>"
#			print "</table>"	
			print "<BR>"	
			m+=1
		print
#for a in I:
#  print a
#  print "<BR><BR>"

##############################_______ACTION TABLE

#actionCount=0
#action=[]
#action.append([])
#action[actionCount].append('state')
#for a in code.terminals:
#  action[actionCount].append(a)
#for a in code.nonterms:
#  action[actionCount].append(a)

#while actionCount<len(I):
#  actionCount+=1
#  action.append([])
#  action[actionCount].append(str(actionCount-1))
#  ruleFlag=False
#  ruleNo=0
#  if len(I[actionCount-1][0])==1:
#    rule=[]
#    for i in range(0,len(I[actionCount-1][0][0])-1):
#      rule.append(I[actionCount-1][0][0][i])
#    #print len(I[actionCount-1][0][0])
#    #for i in I[actionCount-1][0]:
#      #rule.append(i)
#    for r in code.rules:
#      if rule==r:
#	ruleFlag=True
#      ruleNo+=1
#    #if ruleFlag:
#      #print actionCount-1,rule
#  for a in code.terminals:
#    I_1 = calc_goto(I[actionCount-1][0],a)
#    p=0
#    if len(I_1)==0:
#      action[actionCount].append(' ')
#    else:
#      for p in range(0,len(I)):
#	if I[p][0]==I_1:
#	  action[actionCount].append('s'+str(p))
#	  break
#      if p==len(I):
#	action[actionCount].append(' ')

#  for a in code.nonterms:
#    I_1 = calc_goto(I[actionCount-1][0],a)
#    p=0
#    if len(I_1)==0:
#      action[actionCount].append(' ')
#    else:
#      for p in range(0,len(I)):
#	if I[p][0]==I_1:
#	  action[actionCount].append('s'+str(p))
#	  break
#      if p==len(I):
#	action[actionCount].append(' ')

code.terminals.add('$')  
nonterm_initial2_place=place(nonterm_initial2)
  
########################################### Add this code for action table
actionCount=0
action=[]
action.append([])
action[actionCount].append('state')
for a in code.terminals:
  action[actionCount].append(a)
for a in code.nonterms:
  action[actionCount].append(a)

while actionCount<len(I):
  actionCount+=1
  action.append([])
  action[actionCount].append(str(actionCount-1))
  ruleFlag=False
  ruleNo=0
  if len(I[actionCount-1][0])==1:
    rule=[]
    for i in range(0,len(I[actionCount-1][0][0])-1):
      rule.append(I[actionCount-1][0][0][i])
    for r in code.rules:
      if rule==r:
	ruleFlag=True
	break
      ruleNo+=1
    if ruleFlag:
      print actionCount-1,ruleNo,rule
    if ruleFlag:
      for a in code.terminals:
	if a in runner.followNt[nonterm_initial2_place]:
	  action[actionCount].append('r'+str(ruleNo))
	else:
	  action[actionCount].append(' ')
      for a in code.nonterms:
	action[actionCount].append(' ')
  for a in code.terminals:
    I_1 = calc_goto(I[actionCount-1][0],a)
    p=0
    if len(I_1)==0 and not ruleFlag:
      action[actionCount].append(' ')
    else:
      for p in range(0,len(I)):
	if I[p][0]==I_1 and not ruleFlag:
	  action[actionCount].append('s'+str(p))
	  break
      if p==len(I) and not ruleFlag:
	action[actionCount].append(' ')

  for a in code.nonterms:
    I_1 = calc_goto(I[actionCount-1][0],a)
    p=0
    if len(I_1)==0 and not ruleFlag:
      action[actionCount].append(' ')
    else:
      for p in range(0,len(I)):
	if I[p][0]==I_1 and not ruleFlag:
	  action[actionCount].append('s'+str(p))
	  break
      if p==len(I) and not ruleFlag:
	action[actionCount].append(' ')


if(h.ACTION_TABLE=='1'):    
	print "<h1 align=\"center\" >Action and GOTO table</h1>"
	print "<table border=\"3\" align=\"center\">"    
	for a in action:
		print "<tr>\n"
		for i in a:
			print "<td style=\"padding-left: 10px; padding-right: 10px;\">"
			print i
			print "</td>"
		print "</tr>"	
	print "</table>"






