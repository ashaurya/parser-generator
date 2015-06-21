import code as code
import handler as h
import copy

for a in code.firstnt:
	b = a+'prime'
	rule = [b, a]

code.rules.append(rule)

for r in range(len(code.rules)-1, 0, -1):
  code.rules[r]=code.rules[r-1]
code.rules[0]=rule
print "<div class=\"tabcontent\" id=\"cont-1-1\"> <BR>"
print "<h1 align=\"center\" >The rules are:<BR></h1>"

print "<table border=\"3\" align=\"center\">"
for r in code.rules:
	print "<tr>"
	print "<td width=\"100\" align=\"center\"><b>",r[0],"</b></td>"
	print "<td width=\"50\" align=\"center\"> -> </td>"
	print "<td width=\"200\" align=\"center\"><b>" 
	for i in range(1,len(r)):
	  print r[i],
	print "</b></td>"
print "</table>"
print "</p>"
print "</div>"

code.nonterms.add(b)
nonterm_initial=b
nonterm_initial2=a

firstNt = []
firstT = []
for a in range(0, len(code.nonterms)):
	firstNt.append(set())

for a in code.terminals:
	firstT.append(set([a]))
	
def place_sym(a):
	if a in code.terminals:
		i=0
		for b in code.terminals:
			if(a==b):
				return i
				break
			else:
				i = i +1
		else:
			return -1
	else:
		i=0
		for b in code.nonterms:
			if(a==b):
				return i
				break
			else: 
				i = i+1
		else:
			return -1

nonterm_initial2_place_sym=place_sym(nonterm_initial2)

def compute_first(r):
	p = place_sym(r[0])
	if(p==-1):
		print "First element of the rule is not in no terminal set"
		return False
	else:
		old = set(firstNt[p])
		l = len(r)
		i=1
		while(i<l):
			if(r[i] in code.terminals):
				firstNt[p].update(firstT[place_sym(r[i])])
				break
			else:
				if(len(firstNt[place_sym(r[i])])!=0):
					t = set(firstNt[place_sym(r[i])])
					if(' ' in t):
						t.remove(' ')
					firstNt[p].update(t)	
				if(' ' in firstNt[place_sym(r[i])]):
					i = i+1
				else:
					break
		if(firstNt[p]==old):
			return False
		else:
			return True

change = True
while(change):
	change = False
	for r in code.rules:
		c = compute_first(r)
		change = change|c
		
		
		
i=0
print "<div class=\"tabcontent\" id=\"cont-2-1\"> <BR><BR><BR>"
print "<div class=\"content\">"
print "<u>Contents:</u><br />"
print "<a href=\"#first\">1. First Set</a><br />"
print "<a href=\"#follow\">2. Follow Set</a><br />"
print "</div>"
if(h.FIRST=='1'):
	print "<a name=\"first\">"
	print "<h1 align=\"center\" >First Set</h1>"
	print "<table border=\"3\" align=\"center\">"
	for a in code.nonterms:
		print "<tr>"
		print "<td width=\"100\" align=\"center\"><b>",a,"</b></td>"
		print "<td width=\"50\" align=\"center\"> : </td>"
		m=0
		length=len(firstNt[i])
		while(m<length):
			l=list(firstNt[i])[m]
			print "<td width=\"70\" align=\"center\">",l,"</td>"
			m = m+1
		print "</tr>"
		i = i+1
	print "</table></a>"

	print
	print


followNt = []
followNonterm = []
followT = []
for a in range(0,len(code.nonterms)):
	followNt.append(set())
	followNonterm.append([])

for a in code.terminals:
	followT.append(set('$'))

followNt[place_sym(nonterm_initial)].update('$')
followNonterm[place_sym(nonterm_initial)].append('$')

for r in code.rules:
  l=len(r)
  for i in range(2,l):
    if r[i-1] in code.nonterms:
      tmp='First('+r[i]+')'
      if tmp not in followNonterm[place_sym(r[i-1])]:
	followNonterm[place_sym(r[i-1])].append(tmp)
      if r[i] in code.terminals:
	followNt[place_sym(r[i-1])].update(firstT[place_sym(r[i])])
      if r[i] in code.nonterms:
	followNt[place_sym(r[i-1])].update(firstNt[place_sym(r[i])])
      if 'epsilon' in followNt[place_sym(r[i-1])]:
	followNt[place_sym(r[i-1])].remove('epsilon')

	
def computeFirstFollow(r,n):
  l=len(r)
  first = []
  firstSymbol=[]
  for i in range(n,l):
    tmp='First('+r[i]+')'
    first.append(tmp)
    if r[i] in code.nonterms:
      for f in firstNt[place_sym(r[i])]:
	firstSymbol.append(f)
    if r[i] in code.terminals:
      for f in firstT[place_sym(r[i])]:
	firstSymbol.append(f)
    if len(firstNt)>place_sym(r[i]):
      if not 'epsilon' in firstNt[place_sym(r[i])]:
	break
  return first,firstSymbol	

  
def compute_follow(r):
  l=len(r)
  if r[l-1] in code.nonterms:
    tmp='Follow('+r[0]+')'
    if tmp not in followNonterm[place_sym(r[l-1])] and r[l-1]!=r[0]:
      followNonterm[place_sym(r[l-1])].append(tmp)
      followNt[place_sym(r[l-1])].update(followNt[place_sym(r[0])])
    for i in range(1,l-1):
      if r[i] in code.nonterms:
	first,firstSymbol = computeFirstFollow(r,i+1)
	if 'epsilon' in firstSymbol:
	  followNt[place_sym(r[i])].update(followNt[place_sym(r[0])])
	  tmp='Follow('+r[0]+')'
	  if tmp not in followNonterm[place_sym(r[i])] and r[i]!=r[0]:
	    followNonterm[place_sym(r[i])].append(tmp)
	    if 'epsilon' in followNt[place_sym(r[i])]:
	      followNt[place_sym(r[i])].remove('epsilon')
    
    
change=True      
while(change):
  change=False
  oldFollowNonterm = followNonterm
  for r in code.rules:
    compute_follow(r)
  for i in range(0,len(oldFollowNonterm)):
    if not oldFollowNonterm[i]==followNonterm[i]:
      change=True

  
    
i=0
if(h.FOLLOW=='1'):
	print "<a name=\"follow\">"
	print "<h1 align=\"center\" >Follow Set</h1>"
	print "<table border=\"3\" align=\"center\">"
	for a in code.nonterms:
		print "<tr>"
		print "<td width=\"100\" align=\"center\"><b>",a,"</b></td>"
		print "<td width=\"50\" align=\"center\"> : </td>"
		m=0
		length=len(followNt[i])
		while(m<length):
			l=list(followNt[i])[m]
			print "<td width=\"70\" align=\"center\">",l,"</td>"
			m = m+1
		print "</tr>"
		i = i+1
	print "</table></a>"
	print "</div>"
	
	print
	print
    
	
ptable = []
for a in range(0,len(code.nonterms)):
    ptable.append({})

for r in code.rules:
    if r[1] in code.terminals:
        ptable[place_sym(r[0])][r[1]] = r;
        #print 'Here : ', ptable
    elif r[1] in code.nonterms:
        for x in firstNt[place_sym(r[1])]:
            if x in code.terminals:
                ptable[place_sym(r[0])][x] = r;
    if 'epsilon' in firstNt[place_sym(r[0])]:
        for t in followNt[place_sym(r[0])]:
            if t in code.terminals:
                ptable[place_sym(r[0])][t] = r;
        ptable[place_sym(r[0])]['$']=r;


if(h.PARSE_TABLE=='1'):
	print "<div class=\"tabcontent\" id=\"cont-3-1\"> <BR><BR><BR>"
	print "<div class=\"content\">"
	print "<u>Contents:</u><br />"
	print "<a href=\"#ll1_parse\">1. LL(1) Parse Table</a><br />"
	print "</div>"
	print "<a name=\"ll1_parse\">"
	print "<h1 align=\"center\" >Parse Table</h1>"
	print "<table border=\"3\" align=\"center\">"
	print "<tr>"
	print "<td width=\"100\" align=\"center\"></td>"
	print "<td width=\"50\" align=\"center\"></td>"
	for t in code.terminals:
		print "<td align=\"center\"><b>",t,"</b></td>"
	print "<td align=\"center\">\'$\'</td>"
	print "</tr>"
	for i in code.nonterms:
		print "<tr>"
		print "<td width=\"100\" align=\"center\"><b>",i,"</b></td>"
		print "<td width=\"50\" align=\"center\"> : </td>"
		
		for t in code.terminals:
			if ptable[place_sym(i)].has_key(t):
				print "<td width=\"250\" align=\"center\">",ptable[place_sym(i)][t][0]," : ",
				k=0
				for f in ptable[place_sym(i)][t]:
					if (k!=0):
						print ptable[place_sym(i)][t][k],
					k+=1	
				print "</td>"
			else:
				print "<td></td>"
		if ptable[place_sym(i)].has_key('$'):
			print "<td width=\"250\" align=\"center\">",ptable[place_sym(i)]['$'][0]," : ",
			k=0
			for f in ptable[place_sym(i)]['$']:
				if (k!=0):
					print ptable[place_sym(i)]['$'][k],
				k+=1	
			print "</td>"
		else:
			print "<td></td>"
		print "</tr>"	
	print "</table><BR>"
	print "</div>"


    
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

		
for a in code.firstnt:
	b = a+'prime'
	rule = [b, a]

rule.extend('1')
code.rules.append(rule)

I_o = calc_closure(rule)
RULE=copy.deepcopy(rule)
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
	  change=True


goto=[]
p=0
for p in range(0,len(I)):
  for a in code.nonterms:
    I_1=calc_goto(I[p][0],a)
    if len(I_1)!=0:
      for q in range(0,len(I)):
	if I[q][0]==I_1:
	  goto.append([])
	  goto[len(goto)-1].append(p)
	  goto[len(goto)-1].append(a)
	  goto[len(goto)-1].append(q)
	  break
  for a in code.terminals:
    I_1=calc_goto(I[p][0],a)
    if len(I_1)!=0:
      for q in range(0,len(I)):
	if I[q][0]==I_1:
	  goto.append([])
	  goto[len(goto)-1].append(p)
	  goto[len(goto)-1].append(a)
	  goto[len(goto)-1].append(q)
	  break


if(h.CLOSURE=='1'):
	print "<div class=\"tabcontent\" id=\"cont-4-1\"> <BR><BR><BR>"
	print "<div class=\"content\">"
	print "<u>Contents:</u><br />"
	print "<a href=\"#lr0_item\">1. LR(0) Item Sets</a><br />"
	countI=0
	for a in I:
	  for p in a:
	    print "&nbsp;&nbsp;&nbsp;<a href=\"#lr0I_"+str(countI)+"\">1."+str(countI)+" &nbsp;I_"+str(countI)+"</a><br />"
	    countI+=1
	print "<a href=\"#lr0_parseTable\">2. Action and Goto Table</a><br />"
	print "</div>"
	print "<a name=\"lr0_item\">"
	print "<h1 align=\"center\" >LR(0) Item Sets</h1>"
	m=0	
	n=0
	countI=0
	for a in I:
		for p in a:
			print "</a><a name=\"lr0I_"+str(countI)+"\">"
			countI+=1
			print "<BR><h2 align=\"center\" >I_%r <BR>"%m
			flag=1
			for g in goto:
				if g[2]==m:
					if flag==1:
						print "GOTO(I"+str(g[0])+","+g[1]+") "
						flag=0
					else:
						print "= GOTO(I"+str(g[0])+","+g[1]+") "
			print "</h2>"
			   		
			print "<table border=\"3\" align=\"center\">"
			print "<tr>"
			print "<td>"
			print "<table border=\"3\" align=\"center\">"
			k=0
			count=0
			for x in p:
				for e in x:
					if(e.isdigit()):
						k=int(e)
				i=0
				comma=0
				print "<tr>"
				for l in x:
					if(l.isdigit()):
						continue
					if(i==0):
						if(k==1):
							print "<td>%r</td><td>:</td><td> <b>.</b> "%l
						else:
							print "<td>%r</td><td>:</td><td>"%l	
						i=1
						continue
					print l,
					if(i==k-1):
						print " <b>.</b> ",
					i+=1
				print "</td></tr>"
				count+=1
				if (count==int(len(p)/3)+1 and len(p)!=1) or (count==int(2*len(p)/3)+1 and len(p)!=3):
				  print "</table></td><td><table border=\"3\" align=\"center\">"
			print "</table>"	  
			print "</td></tr></table></a>"
			print "<BR>"	
			m+=1
		print

		
  
code.terminals.add('$')  
  
  
lr0_actionCount=0
lr0_action=[]
lr0_action.append([])
lr0_action[lr0_actionCount].append('state')
for a in code.terminals:
  lr0_action[lr0_actionCount].append(a)
for a in code.nonterms:
  if a!=nonterm_initial:
    lr0_action[lr0_actionCount].append(a)
  
for i in range(0,len(I)):
  lr0_action.append([])
  lr0_action[i+1].append([])
  for a in code.terminals:
    lr0_action[i+1].append([])
  for a in code.nonterms:
    if a!=nonterm_initial:
      lr0_action[i+1].append([])
  
while lr0_actionCount<len(I):
  lr0_actionCount+=1
  count=0
  lr0_action[lr0_actionCount][count].append(str(lr0_actionCount-1))
  count+=1
  for a in code.terminals:
    I_1 = calc_goto(I[lr0_actionCount-1][0],a)
    p=0
    if len(I_1)==0:
      count+=1
    else:
      for p in range(0,len(I)):
	if I[p][0]==I_1:
	  lr0_action[lr0_actionCount][count].append('s'+str(p))
	  count+=1
	  break
      if p==len(I):
	count+=1

  for a in code.nonterms:
    if a==nonterm_initial:
      continue
    I_1 = calc_goto(I[lr0_actionCount-1][0],a)
    p=0
    if len(I_1)==0:
      count+=1
    else:
      for p in range(0,len(I)):
	if I[p][0]==I_1:
	  lr0_action[lr0_actionCount][count].append(str(p))
	  count+=1
	  break
      if p==len(I):
	count+=1
	
  for index in I[lr0_actionCount-1][0]:
    if str(len(index)-1)==index[len(index)-1]:
      ruleFlag=False
      ruleNo=0
      rule=[]
      for i in range(0,len(index)-1):
	rule.append(index[i])
      for r in code.rules:
	if rule==r:
	  ruleFlag=True
	  break
	ruleNo+=1
      if ruleFlag:
	A=index[0]
	count=1
	for a in code.terminals:
	  if not A==nonterm_initial:
	    if a=='$':
	      lr0_action[lr0_actionCount][count].append('r'+str(ruleNo))
	    elif not a=='$':
	      lr0_action[lr0_actionCount][count].append('r'+str(ruleNo))
	  count+=1

I_1=calc_goto(I[0][0],nonterm_initial2)
p=0
for p in range(0,len(I)):
  if I[p][0]==I_1:
    break
for a in range(0,len(lr0_action[p+1])):
  if lr0_action[0][a]=='$':
    lr0_action[p+1][a].append("acc")
    break

for i in range(1,len(I)+1):
  for j in range(1,len(lr0_action[i])):
    if len(lr0_action[i][j])==0:
      lr0_action[i][j].append(' ')
    

if(h.ACTION_TABLE=='1'):    
	print "<a name=\"lr0_parseTable\">"
	print "<h1 align=\"center\" >LR(0) Action and GOTO table</h1>"
	print "<table border=\"3\" align=\"center\">"    
	print "<tr>\n"
	for i in lr0_action[0]:
		print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>"
		print i
		print "</b></center></td>"
	print "</tr>"	
	for a in range(1,len(lr0_action)):
		print "<tr>\n"
		c=0
		for i in lr0_action[a]:
			print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center>"
			#print i
			if c==0:
			  c=1
			  print "<b>"
			  for k in range(0,len(i)-1):
			    print i[k]+',',
			  print i[len(i)-1]
			  print "</b>"
			else:
			  for k in range(0,len(i)-1):
			    print i[k]+',',
			  print i[len(i)-1]
			print "</center></td>"
		print "</tr>"	
	print "</table></a>"
	print "</div>"

print "<BR>"  
  
  
  
actionCount=0
action=[]
action.append([])
action[actionCount].append('state')
for a in code.terminals:
  action[actionCount].append(a)
for a in code.nonterms:
  if a!=nonterm_initial:
    action[actionCount].append(a)
  
for i in range(0,len(I)):
  action.append([])
  action[i+1].append([])
  for a in code.terminals:
    action[i+1].append([])
  for a in code.nonterms:
    if a!=nonterm_initial:
      action[i+1].append([])
  
while actionCount<len(I):
  actionCount+=1
  count=0
  action[actionCount][count].append(str(actionCount-1))
  count+=1
  for a in code.terminals:
    I_1 = calc_goto(I[actionCount-1][0],a)
    p=0
    if len(I_1)==0:
      count+=1
    else:
      for p in range(0,len(I)):
	if I[p][0]==I_1:
	  action[actionCount][count].append('s'+str(p))
	  count+=1
	  break
      if p==len(I):
	count+=1

  for a in code.nonterms:
    if a==nonterm_initial:
      continue
    I_1 = calc_goto(I[actionCount-1][0],a)
    p=0
    if len(I_1)==0:
      count+=1
    else:
      for p in range(0,len(I)):
	if I[p][0]==I_1:
	  action[actionCount][count].append(str(p))
	  count+=1
	  break
      if p==len(I):
	count+=1
	
  for index in I[actionCount-1][0]:
    if str(len(index)-1)==index[len(index)-1]:
      ruleFlag=False
      ruleNo=0
      rule=[]
      for i in range(0,len(index)-1):
	rule.append(index[i])
      for r in code.rules:
	if rule==r:
	  ruleFlag=True
	  break
	ruleNo+=1
      if ruleFlag:
	A=index[0]
	count=1
	for a in code.terminals:
	  if a in followNt[place_sym(A)] and not A==nonterm_initial:
	    if a=='$':
	      action[actionCount][count].append('r'+str(ruleNo))
	    elif not a=='$':
	      action[actionCount][count].append('r'+str(ruleNo))
	  count+=1

I_1=calc_goto(I[0][0],nonterm_initial2)
p=0
for p in range(0,len(I)):
  if I[p][0]==I_1:
    break
for a in range(0,len(action[p+1])):
  if action[0][a]=='$':
    action[p+1][a].append("acc")
    break

for i in range(1,len(I)+1):
  for j in range(1,len(action[i])):
    if len(action[i][j])==0:
      action[i][j].append(' ')
    
    
if(h.ACTION_TABLE=='1'):
	print "<div class=\"tabcontent\" id=\"cont-6-1\"> <BR><BR>"
	print "<div class=\"content\">"
	print "<u>Contents:</u><br />"
	print "<a href=\"#slr0_parseTable\">1. Action and Goto Table</a><br />"
	print "</div>"
	print "<a name=\"slr0_parseTable\">"
	print "<h1 align=\"center\" >SLR(1) Action and GOTO table</h1>"
	print "<table border=\"3\" align=\"center\">"    
	print "<tr>\n"
	for i in action[0]:
		print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>"
		print i
		print "</b></center></td>"
	print "</tr>"	
	for a in range(1,len(action)):
		print "<tr>\n"
		c=0
		for i in action[a]:
			print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center>"
			if c==0:
			  c=1
			  print "<b>"
			  for k in range(0,len(i)-1):
			    print i[k]+',',
			  print i[len(i)-1]
			  print "</b>"
			else:
			  for k in range(0,len(i)-1):
			    print i[k]+',',
			  print i[len(i)-1]
			print "</center></td>"
		print "</tr>"	
	print "</table></a>"
	print "</div>"

print "<BR>"


RULE.append('$')
def LR_calc_closure(item):
	closure = []
	closure.append(item)
	change = 1
	while(change==1):
		change = 0
		for _item_ in closure:
			place = int(_item_[len(_item_)-2])
			if(place >= len(_item_)-2 or place==0):
				break
			else:
				if(_item_[place] in code.nonterms):
					for a in code.rules:
						if(_item_[place]==a[0]):
							if(_item_[place] in code.nonterms):
								if ((_item_[place+1] not in list(code.terminals)) and ('epsilon' in firstNt[place_sym(_item_[place+1])]) or (_item_[place+1].isdigit())):
									temp = []
									temp.extend(a)
									temp.extend('1')
									if(len(_item_[len(_item_)-1])>1):
										temp.append('')
										temp[len(temp)-1]=_item_[len(_item_)-1]
									else:	
										temp.extend(_item_[len(_item_)-1])
									for l in range(0, len(closure)):
										if(temp==closure[l]):
											break
									else:
										closure.append(temp)
										change= 1
								if(_item_[place+1] in list(code.terminals)):
									temp = []
									temp.extend(a)
									temp.extend('1')
									if(len(_item_[place+1])>1):
										temp.append('')
										temp[len(temp)-1]=_item_[place+1]
									else:	
										temp.extend(_item_[place+1])
									for l in range(0, len(closure)):
										if(temp==closure[l]):
											break
									else:
										closure.append(temp)
										change= 1
								if(_item_[place+1] in code.nonterms):
									for q in firstNt[place_sym(_item_[place+1])]:
										temp = []
										temp.extend(a)
										temp.extend('1')
										if(len(q)>1):
											temp.append('')
											temp[len(temp)-1]=q
										else:	
											temp.extend(q)
										for l in range(0, len(closure)):
											if(temp==closure[l]):
												break
										else:
											closure.append(temp)
											change= 1
	return closure


LR_I_o=LR_calc_closure(RULE)

def LR_calc_goto(set_prod, var):
	set_ret = []
	for rule_no in range(0, len(set_prod)):
		rule = set_prod[rule_no]
		l = len(rule)
		for a in range(1, l-1):
			if(var==rule[a] and a==int(rule[l-2])):
				temp = []
				temp.extend(rule)
				temp[l-2] = str(int(temp[l-2])+1)
				c = LR_calc_closure(temp)
				for b in range(0, len(c)):
					for r in range(0, len(set_ret)):
						if(c[b]==set_ret[r]):
							break
					else:
						set_ret.append(c[b])
	return set_ret


def same(a,b):
	lena=len(a)
	lenb=len(b)
	same_or_not=False
	if(lena==lenb):
		rule_count=0
		for i in range(0,lena):
			for j in range(0,lena):
				if(a[i]==b[j]):
					rule_count+=1
		if(rule_count==lena):
			same_or_not=True
	return same_or_not
						
LR_I=[]
LR_I.append([])
LR_I[len(LR_I)-1].append(LR_I_o)
change=True
while change==True:
  change=False
  for LR_I_o in LR_I:
    for a in code.nonterms:
      LR_I_1=LR_calc_goto(LR_I_o[0],a)
      c=False
      if len(LR_I_1)!=0:
	for p in LR_I:
	  if same(p[0],LR_I_1):
	    c=True
	if c==False:
	  LR_I.append([])
	  LR_I[len(LR_I)-1].append(LR_I_1)
	  change=True
    for a in code.terminals:
      LR_I_1=LR_calc_goto(LR_I_o[0],a)
      c=False
      if len(LR_I_1)!=0:
	for p in LR_I:
	  if same(p[0],LR_I_1):
	    c=True
	if c==False:
	  LR_I.append([])
	  LR_I[len(LR_I)-1].append(LR_I_1)
	  change=True


delete=[]
for i in range(0,len(LR_I)):
	for j in range(i+1,len(LR_I)):
		len_ori=len(LR_I[i][0])
		len_cop=len(LR_I[j][0])
		if(len_ori==len_cop):
			rule_count=0
			for k in range(0,len_ori):
				for l in range(0,len_ori):
					u=len(LR_I[i][0][k])
					v=len(LR_I[j][0][l])
					if(u==v):
						if(LR_I[i][0][k]==LR_I[j][0][l]):
#							print "SAME"
							rule_count+=1
			if(rule_count==len_ori):
				delete.append(j)	
							
delete=sorted(delete,reverse=True)
for a in delete:
	LR_I.remove(LR_I[a])
	
LR_goto=[]
p=0
for p in range(0,len(LR_I)):
  for a in code.nonterms:
    LR_I_1=LR_calc_goto(LR_I[p][0],a)
    if len(LR_I_1)!=0:
      for q in range(0,len(LR_I)):
	if same(LR_I[q][0],LR_I_1):
	  LR_goto.append([])
	  LR_goto[len(LR_goto)-1].append(p)
	  LR_goto[len(LR_goto)-1].append(a)
	  LR_goto[len(LR_goto)-1].append(q)
	  break
  for a in code.terminals:
    LR_I_1=LR_calc_goto(LR_I[p][0],a)
    if len(LR_I_1)!=0:
      for q in range(0,len(LR_I)):
	if same(LR_I[q][0],LR_I_1):
	  LR_goto.append([])
	  LR_goto[len(LR_goto)-1].append(p)
	  LR_goto[len(LR_goto)-1].append(a)
	  LR_goto[len(LR_goto)-1].append(q)
	  break

	  
if(h.LRCLOSURE=='1'):
	print "<div class=\"tabcontent\" id=\"cont-5-1\"><BR>"
	print "<div class=\"content\">"
	print "<u>Contents:</u><br />"
	print "<a href=\"#lr1_item\">1. LR(1) Item Sets</a><br />"
	countI=0
	for a in LR_I:
	  for p in a:
	    print "&nbsp;&nbsp;&nbsp;<a href=\"#lr1I_"+str(countI)+"\">1."+str(countI)+" &nbsp;I_"+str(countI)+"</a><br />"
	    countI+=1
	print "<a href=\"#lr1_parseTable\">2. Action and Goto Table</a><br />"
	print "</div>"
	print "<a name=\"lr1_item\">"
	print "<h1 align=\"center\" >LR(1) Item Sets</h1></a>"
	m=0	
	n=0
	countI=0
	for a in LR_I:
		for p in a:
			print "</a><a name=\"lr1I_"+str(countI)+"\">"
			countI+=1
			print "<BR><h2 align=\"center\" >I_%r <BR>"%m
			flag=1
			for g in LR_goto:
				if g[2]==m:
					if flag==1:
						print "GOTO(I"+str(g[0])+","+g[1]+") "
						flag=0
					else:
						print "= GOTO(I"+str(g[0])+","+g[1]+") "
			print "</h2>"
			   		
			print "<table border=\"3\" align=\"center\">"
			print "<tr>"
			print "<td>"
			print "<table border=\"3\" align=\"center\">"
			k=0
			count=0
			for x in p:
				for e in x:
					if(e.isdigit()):
						k=int(e)
				i=0
				comma=0
				print "<tr>"
				for l in x:
					if(l.isdigit()):
						continue
					if(i==0):
						if(k==1):
							print "<td>%r</td><td>:</td><td> <b>.</b> "%l
						else:
							print "<td>%r</td><td>:</td><td>"%l	
						i=1
						continue
					print l,
					if(i==k-1):
						print " <b>.</b> ",
					i+=1
				print "</td></tr>"
				count+=1
				if (count==int(len(p)/3)+1 and len(p)!=1) or (count==int(2*len(p)/3)+1 and len(p)!=3):
				  print "</table></td><td><table border=\"3\" align=\"center\">"
			print "</table>"	  
			print "</td></tr></table></a>"
			print "<BR>"	
			m+=1
		print



LRactionCount=0
LR_action=[]
LR_action.append([])
LR_action[LRactionCount].append('state')
for a in code.terminals:
  LR_action[LRactionCount].append(a)
for a in code.nonterms:
  if a!=nonterm_initial:
    LR_action[LRactionCount].append(a)
  
for i in range(0,len(LR_I)):
  LR_action.append([])
  LR_action[i+1].append([])
  for a in code.terminals:
    LR_action[i+1].append([])
  for a in code.nonterms:
    if a!=nonterm_initial:
      LR_action[i+1].append([])
  
while LRactionCount<len(LR_I):
  LRactionCount+=1
  count=0
  LR_action[LRactionCount][count].append(str(LRactionCount-1))
  count+=1
  for a in code.terminals:
    LR_I_1 = LR_calc_goto(LR_I[LRactionCount-1][0],a)
    p=0
    if len(LR_I_1)==0:
      count+=1
    else:
      for p in range(0,len(LR_I)):
  	if same(LR_I[p][0],LR_I_1):
	  LR_action[LRactionCount][count].append('s'+str(p))
	  count+=1
	  break
      if p==len(LR_I):
	count+=1

  for a in code.nonterms:
    if a==nonterm_initial:
      continue
    LR_I_1 = LR_calc_goto(LR_I[LRactionCount-1][0],a)
    p=0
    if len(LR_I_1)==0:
      count+=1
    else:
      for p in range(0,len(LR_I)):
	if same(LR_I[p][0],LR_I_1):
	  LR_action[LRactionCount][count].append(str(p))
	  count+=1
	  break
      if p==len(LR_I):
	count+=1
	
  for index in LR_I[LRactionCount-1][0]:
    if str(len(index)-1)==index[len(index)-1]:
      ruleFlag=False
      ruleNo=0
      rule=[]
      for i in range(0,len(index)-1):
	rule.append(index[i])
      for r in code.rules:
	if rule==r:
	  ruleFlag=True
	  break
	ruleNo+=1
      if ruleFlag:
	print LRactionCount-1,ruleNo,rule
	A=index[0]
	count=1

	
LR_I_1=LR_calc_goto(LR_I[0][0],nonterm_initial2)
p=0
for p in range(0,len(LR_I)):
  if same(LR_I[p][0],LR_I_1):
    break
for a in range(0,len(LR_action[p+1])):
  if LR_action[0][a]=='$':
    LR_action[p+1][a].append("acc")
    break

    
    
tcount=0	
for a in code.terminals:
	tcount+=1
	for p in range(0,len(LR_I)):
		for r in range(0,len(LR_I[p])):
			for k in range(0,len(LR_I[p][r])):
				if(int(LR_I[p][r][k][len(LR_I[p][r][k])-2])==len(LR_I[p][r][k])-2 and (LR_I[p][r][k][0]!=nonterm_initial) and LR_I[p][r][k][len(LR_I[p][r][k])-1]==a):
					number=0
					string="5"
					for R in code.rules:
						if(R == LR_I[p][r][k][:-2]):
							string="r"+str(number)
						number+=1
					if(len(LR_action[p+1][tcount])==0):		
						LR_action[p+1][tcount].append(string)
					

for i in range(1,len(LR_I)+1):
  for j in range(1,len(LR_action[i])):
    if len(LR_action[i][j])==0:
      LR_action[i][j].append(' ')
    
    
if(h.LRACTION_TABLE=='1'): 
	print "<a name=\"lr1_parseTable\">"
	print "<h1 align=\"center\" >LR(1) Action and GOTO table</h1>"
	print "<table border=\"3\" align=\"center\">"    
	print "<tr>\n"
	for i in LR_action[0]:
		print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>"
		print i
		print "</b></center></td>"
	print "</tr>"	
	for a in range(1,len(LR_action)):
		print "<tr>\n"
		c=0
		for i in LR_action[a]:
			print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center>"
			if c==0:
			  print "<b>"
			  for k in range(0,len(i)-1):
			    print i[k]+',',
			  print i[len(i)-1]
			  print "</b>"
			  c=1
			else:
			  for k in range(0,len(i)-1):
			    print i[k]+',',
			  print i[len(i)-1]
			print "</center></td>"
		print "</tr>"	
	print "</table></a>"
	print "</div>"

print "<BR>"



def LA_calc_closure(item):
	closure = []
	closure.append(item)
	change = 1
	while(change==1):
		change = 0
		for _item_ in closure:
			place = int(_item_[len(_item_)-2])
			if(place >= len(_item_)-2 or place==0):
				break
			else:
				if(_item_[place] in code.nonterms):
					for a in code.rules:
						if(_item_[place]==a[0]):
							if(_item_[place] in code.nonterms):
								if ((_item_[place+1] not in list(code.terminals)) and ('epsilon' in firstNt[place_sym(_item_[place+1])]) or (_item_[place+1].isdigit())):
									temp = []
									temp.extend(a)
									temp.extend('1')
									if(len(_item_[len(_item_)-1])>1):
										temp.append('')
										temp[len(temp)-1]=_item_[len(_item_)-1]
									else:	
										temp.extend(_item_[len(_item_)-1])
									for l in range(0, len(closure)):
										if(temp==closure[l]):
											break
									else:
										closure.append(temp)
										change= 1
								if(_item_[place+1] in list(code.terminals)):
									temp = []
									temp.extend(a)
									temp.extend('1')
									if(len(_item_[place+1])>1):
										temp.append('')
										temp[len(temp)-1]=_item_[place+1]
									else:	
										temp.extend(_item_[place+1])
									for l in range(0, len(closure)):
										if(temp==closure[l]):
											break
									else:
										closure.append(temp)
										change= 1
								if(_item_[place+1] in code.nonterms):
									for q in firstNt[place_sym(_item_[place+1])]:
										temp = []
										temp.extend(a)
										temp.extend('1')
										if(len(q)>1):
											temp.append('')
											temp[len(temp)-1]=q
										else:	
											temp.extend(q)
										for l in range(0, len(closure)):
											if(temp==closure[l]):
												break
										else:
											closure.append(temp)
											change= 1

	return closure

	
LA_I_o=LA_calc_closure(RULE)

def LA_calc_goto(set_prod, var):
	set_ret = []
	for rule_no in range(0, len(set_prod)):
		rule = set_prod[rule_no]
		l = len(rule)
		for a in range(1, l-1):
			if(var==rule[a] and a==int(rule[l-2])):
				temp = []
				temp.extend(rule)
				temp[l-2] = str(int(temp[l-2])+1)
				c = LA_calc_closure(temp)
				for b in range(0, len(c)):
					for r in range(0, len(set_ret)):
						if(c[b]==set_ret[r]):
							break
					else:
						set_ret.append(c[b])
	return set_ret


def samecore(a,b):
	lena=len(a)
	lenb=len(b)
	a_same_or_not=False
	b_same_or_not=False
	if(1==1):	
		rule_count=0
		for i in range(0,lena):
			for j in range(0,lenb):
				if(a[i][:-1]==b[j][:-1]):
					rule_count+=1
					break
		if(rule_count==lena):
			a_same_or_not=True
	if(1==1):	
		rule_count=0
		for i in range(0,lenb):
			for j in range(0,lena):
				if(a[j][:-1]==b[i][:-1]):
					rule_count+=1
					break
		if(rule_count==lenb):
			b_same_or_not=True
	if(a_same_or_not==True and b_same_or_not==True):
		return True
	else:
		return False			
						
LA_I=[]
LA_I.append([])
LA_I[len(LA_I)-1].append(LA_I_o)
change=True
while change==True:
  change=False
  for LA_I_o in LA_I:
    for a in code.nonterms:
      LA_I_1=LA_calc_goto(LA_I_o[0],a)
      c=False
      if len(LA_I_1)!=0:
	for p in LA_I:
	  if same(p[0],LA_I_1):
	    c=True
	if c==False:
	  LA_I.append([])
	  LA_I[len(LA_I)-1].append(LA_I_1)
	  change=True
    for a in code.terminals:
      LA_I_1=LA_calc_goto(LA_I_o[0],a)
      c=False
      if len(LA_I_1)!=0:
	for p in LA_I:
	  if same(p[0],LA_I_1):
	    c=True
	if c==False:
	  LA_I.append([])
	  LA_I[len(LA_I)-1].append(LA_I_1)
	  change=True

	  
merged=[]
for a in range(0,len(I)):
	merged.append([])

delete=[]
mLA_I=copy.deepcopy(LA_I)
for a in range(0,len(mLA_I)):
	for b in range(a+1,len(mLA_I)):
		if(a!=b):
			if(samecore(mLA_I[a][0],mLA_I[b][0])):
				for x in mLA_I[b][0]:
					mLA_I[a][0].append(x)
				delete.append(b)

delete=list(set(delete))
delete=sorted(delete,reverse=True)
for a in delete:
	mLA_I.remove(mLA_I[a])

for a in range(0,len(mLA_I)):
	delete=[]
	if(1==1):
		for x in range(0,len(mLA_I[a][0])):
			for y in range(x+1,len(mLA_I[a][0])):
				if(x!=y):
					if(mLA_I[a][0][x]==mLA_I[a][0][y]):
						delete.append(y)
	delete=list(set(delete))
	delete=sorted(delete,reverse=True)
	for d in delete:
		mLA_I[a][0].pop(d)


LA_goto=[]
p=0
for p in range(0,len(LA_I)):
  for a in code.nonterms:
    LA_I_1=LA_calc_goto(LA_I[p][0],a)
    if len(LA_I_1)!=0:
      for q in range(0,len(LA_I)):
	if same(LA_I[q][0],LA_I_1):
	  LA_goto.append([])
	  LA_goto[len(LA_goto)-1].append(p)
	  LA_goto[len(LA_goto)-1].append(a)
	  LA_goto[len(LA_goto)-1].append(q)
	  break
  for a in code.terminals:
    LA_I_1=LA_calc_goto(LA_I[p][0],a)
    if len(LA_I_1)!=0:
      for q in range(0,len(LA_I)):
	if same(LA_I[q][0],LA_I_1):
	  LA_goto.append([])
	  LA_goto[len(LA_goto)-1].append(p)
	  LA_goto[len(LA_goto)-1].append(a)
	  LA_goto[len(LA_goto)-1].append(q)
	  break

cLA_I=copy.deepcopy(mLA_I)
for a in range(0,len(mLA_I)):
	for b in range(0,len(mLA_I[a][0])):
		mLA_I[a][0][b].append([])
		mLA_I[a][0][b][len(mLA_I[a][0][b])-1].append(mLA_I[a][0][b][len(mLA_I[a][0][b])-2])
		mLA_I[a][0][b].pop(len(mLA_I[a][0][b])-2)

for a in mLA_I:
	for b in range(0,len(a[0])):
		for c in range(b+1,len(a[0])):
			if(b!=c):
				if(a[0][b][:-1]==a[0][c][:-1]):
					for x in a[0][c][len(a[0][c])-1]: 
						if x not in a[0][b][len(a[0][b])-1]: 
							a[0][b][len(a[0][b])-1].append(x)				

for a in range(0,len(mLA_I)):
	delete=[]
	if(1==1):
		for x in range(0,len(mLA_I[a][0])):
			for y in range(x+1,len(mLA_I[a][0])):
				if(x!=y):
					if(mLA_I[a][0][x][:-1]==mLA_I[a][0][y][:-1]):
						delete.append(y)
	delete=list(set(delete))
	delete=sorted(delete,reverse=True)
	for d in delete:
		mLA_I[a][0].pop(d)


mLA_goto=[]
p=0
for p in range(0,len(mLA_I)):
  for a in code.nonterms:
    mLA_I_1=LA_calc_goto(mLA_I[p][0],a)
    if len(mLA_I_1)!=0:
      for q in range(0,len(mLA_I)):
	if samecore(mLA_I[q][0],mLA_I_1):
	  mLA_goto.append([])
	  mLA_goto[len(mLA_goto)-1].append(p)
	  mLA_goto[len(mLA_goto)-1].append(a)
	  mLA_goto[len(mLA_goto)-1].append(q)
	  break
  for a in code.terminals:
    mLA_I_1=LA_calc_goto(mLA_I[p][0],a)
    if len(mLA_I_1)!=0:
      for q in range(0,len(mLA_I)):
	if samecore(mLA_I[q][0],mLA_I_1):
	  mLA_goto.append([])
	  mLA_goto[len(mLA_goto)-1].append(p)
	  mLA_goto[len(mLA_goto)-1].append(a)
	  mLA_goto[len(mLA_goto)-1].append(q)
	  break



if(h.LACLOSURE=='1'):	
#if(1==1):
	print "<div class=\"tabcontent\" id=\"cont-7-1\">"
	print "<div class=\"content\">"
	print "<u>Contents:</u><br />"
	print "<a href=\"#lalr_item\">1. LALR Item Sets</a><br />"
	countI=0
	for a in mLA_I:
	  for p in a:
	    print "&nbsp;&nbsp;&nbsp;<a href=\"#lalrI_"+str(countI)+"\">1."+str(countI)+" &nbsp;I_"+str(countI)+"</a><br />"
	    countI+=1
	if(1==2):
	  print "<a href=\"#lalr_parseTable\">2. Action and Goto Table</a><br />"
	print "</div>"
	print "<a name=\"lalr_item\">"
	print "<h1 align=\"center\" >LALR Item Sets</h1>"
	m=0	
	n=0
	countI=0
	for a in mLA_I:
		for p in a:
			print "</a><a name=\"lalrI_"+str(countI)+"\">"
			countI+=1
			print "<BR><h2 align=\"center\" >I_%r <BR>"%m
			flag=1
			for g in mLA_goto:
				if g[2]==m:
					if flag==1:
						print "GOTO(I"+str(g[0])+","+g[1]+") "
						flag=0
					else:
						print "= GOTO(I"+str(g[0])+","+g[1]+") "
			print "</h2>"
			   		
			print "<table border=\"3\" align=\"center\">"
			print "<tr>"
			print "<td>"
			print "<table border=\"3\" align=\"center\">"
			k=0
			count=0
			for x in p:
				for e in x:
					if(e.isdigit()):
						k=int(e)
						break
				i=0
				comma=0
				print "<tr>"
				for l in x[:-1]:
					if(l!=x[-1] and l.isdigit()):
						print "</td><td>",
						continue
					if(i==0):
						if(k==1):
							print "<td>%r</td><td>:</td><td> <b>.</b> "%l
						else:
							print "<td>%r</td><td>:</td><td>"%l	
						i=1
						continue
					print l,
					if(i==k-1):
						print " <b>.</b> ",
					i+=1
				for l in x[-1]:
					print l,
					if(l!=x[-1][-1]):
						print " , ",	
				print "</td></tr>"
				count+=1
				if (count==int(len(p)/2)+1 and len(p)!=1):
				  print "</table></td><td><table border=\"3\" align=\"center\">"
			print "</table>"
			print "</td></tr></table></a>"
			print "<BR>"	
			m+=1
		print


mLAactionCount=0
mLA_action=[]
mLA_action.append([])
mLA_action[mLAactionCount].append('state')
for a in code.terminals:
  mLA_action[mLAactionCount].append(a)
for a in code.nonterms:
  if a!=nonterm_initial:
    mLA_action[mLAactionCount].append(a)
  
for i in range(0,len(mLA_I)):
  mLA_action.append([])
  mLA_action[i+1].append([])
  for a in code.terminals:
    mLA_action[i+1].append([])
  for a in code.nonterms:
    if a!=nonterm_initial:
      mLA_action[i+1].append([])
  
while mLAactionCount<len(mLA_I):
  mLAactionCount+=1
  count=0
  mLA_action[mLAactionCount][count].append(str(mLAactionCount-1))
  count+=1
  for a in code.terminals:
    mLA_I_1 = LR_calc_goto(mLA_I[mLAactionCount-1][0],a)
    p=0
    if len(mLA_I_1)==0:
      count+=1
    else:
      for p in range(0,len(mLA_I)):
  	if samecore(mLA_I[p][0],mLA_I_1):
	  mLA_action[mLAactionCount][count].append('s'+str(p))
	  count+=1
	  break
      if p==len(mLA_I):
	count+=1

  for a in code.nonterms:
    if a==nonterm_initial:
      continue
    mLA_I_1 = LR_calc_goto(mLA_I[mLAactionCount-1][0],a)
    p=0
    if len(mLA_I_1)==0:
      count+=1
    else:
      for p in range(0,len(mLA_I)):
	if samecore(mLA_I[p][0],mLA_I_1):
	  mLA_action[mLAactionCount][count].append(str(p))
	  count+=1
	  break
      if p==len(mLA_I):
	count+=1
	
  for index in mLA_I[mLAactionCount-1][0]:
    if str(len(index)-1)==index[len(index)-1]:
      ruleFlag=False
      ruleNo=0
      rule=[]
      for i in range(0,len(index)-1):
	rule.append(index[i])
      for r in code.rules:
	if rule==r:
	  ruleFlag=True
	  break
	ruleNo+=1
      if ruleFlag:
	print mLAactionCount-1,ruleNo,rule
	A=index[0]
	count=1
	
	
mLA_I_1=LR_calc_goto(mLA_I[0][0],nonterm_initial2)
p=0
for p in range(0,len(mLA_I)):
  if samecore(mLA_I[p][0],mLA_I_1):
    break
for a in range(0,len(mLA_action[p+1])):
  if mLA_action[0][a]=='$':
    mLA_action[p+1][a].append("acc")
    break


tcount=0	
for a in code.terminals:
	tcount+=1
	for p in range(0,len(mLA_I)):
		for r in range(0,len(mLA_I[p])):
			for k in range(0,len(mLA_I[p][r])):
				if(int(mLA_I[p][r][k][len(mLA_I[p][r][k])-2])==len(mLA_I[p][r][k])-2 and (mLA_I[p][r][k][0]!=nonterm_initial) and a in mLA_I[p][r][k][len(mLA_I[p][r][k])-1]):
					number=0
					string="empty"
					for R in code.rules:
						if(R == mLA_I[p][r][k][:-2]):
							string="r"+str(number)
							mLA_action[p+1][tcount].append(string)						
						number+=1
					

for i in range(1,len(mLA_I)+1):
  for j in range(1,len(mLA_action[i])):
    if len(mLA_action[i][j])==0:
      mLA_action[i][j].append(' ')
    
if(1==2):
	print "<a name=\"lalr_parseTable\">"
	print "<h1 align=\"center\" >mLA(1) Action and GOTO table</h1>"
	print "<table border=\"3\" align=\"center\">"    
	print "<tr>\n"
	for i in mLA_action[0]:
		print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center>"
		print i
		print "</center></td>"
	print "</tr>"	
	for a in range(1,len(mLA_action)):
		print "<tr>\n"
		for i in mLA_action[a]:
			print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center>"
			#print i
			for k in range(0,len(i)-1):
			  print i[k]+',',
			print i[len(i)-1]
			print "</center></td>"
		print "</tr>"	
	print "</table></a>"

print "</div>"

#print "Program finished\n"	