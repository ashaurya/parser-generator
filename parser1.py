import code as code
import run_parse as run
import handler as h

class Stack:
  def __init__(self) :
    self.items = []

  def top(self):
    tmp=self.items.pop()
    self.items.append(tmp)
    return tmp
  
  def push(self, item) :
    self.items.append(item)

  def pop(self) :
    return self.items.pop()

  def isEmpty(self) :
    return (self.items == [])

    
def value(a):
  for i in range(0,len(run.LR_action[0])):
    if a==run.LR_action[0][i]:
      return i
  return -1

############### Input[] contains the input grammar
#Input=['id',"'*'",'id',"'+'",'id','$']
if(h.expression1=='1'):
	print "<a name=\"lr1_parsing\">"
	linestring = open('expression.txt', 'r').read()
	Input=linestring.split()
	print "<h1 align=\"center\" >LR(1) Parsing</h1><h2><center>Input: "
	for a in Input:
	  print a
	print "</center></h2>"

	input_val=0
	a = Input[input_val]
	S = Stack()
	S.push(0)
	S1=S
	while S1.isEmpty():
	  print S1.pop()
	#print code.rules[4]
	#for k in range(1,len(run.LR_action[9][5])):
	    #print int(run.LR_action[9][5][k])
	print "<table border=\"3\" align=\"center\">"
	print "<tr><td style=\"padding-left: 10px; padding-right: 10px;\"><center>" "</center></td><td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>Stack</b></center></td><td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>Symbol</b></center></td><td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>Input</b></center></td><td style=\"padding-left: 10px; padding-right: 10px;\"><center><b>Action</b></center></td></tr>"
	count=1
	while True:
	  tmp_s=Stack()
	  l=[]
	  print "<tr>\n"
	  print "<td style=\"padding-left: 10px; padding-right: 10px;\"><center>("+str(count)+")</center></td>"
	  count+=1
	  while not S.isEmpty():
	    tmp_s.push(S.pop())
	  print "<td style=\"padding-left: 10px; padding-right: 10px;\">"
	  while not tmp_s.isEmpty():
	    S.push(tmp_s.top())
	    print tmp_s.pop(),
	    f=False
	    if S.top()!=0:
	      for i in range(1,len(run.LR_action)):
		for j in range(1,len(run.LR_action[i])):
		  #print i,j,
		  if 's'+str(S.top()) in run.LR_action[i][j] or str(S.top()) in run.LR_action[i][j]:
		    l.append(run.LR_action[0][j])
		    f=True
		    break
		if f:
		  break
	  print "</td>\n"
	  print "<td style=\"padding-left: 10px; padding-right: 10px;\">"
	  for i in l:
	    print i
	  print "</td>\n"
	  print "<td style=\"padding-left: 10px; padding-right: 10px; text-align: right;\">"
	  for i in range(input_val,len(Input)):
	    print Input[i],
	  print "</td>\n"
	  s=int(S.top()+1)
	  #print s,a,run.LR_action[s][value(a)],"\t",
	  #print input_val,s,
	  #print value(a),
	  print "<td style=\"padding-left: 10px; padding-right: 10px;\">"
	  if run.LR_action[s][value(a)][0][0]=='s':
	    print "shift"
	    t=0
	    for k in range(1,len(run.LR_action[s][value(a)][0])):
	      t=t*10+int(run.LR_action[s][value(a)][0][k])
	    #print t
	    S.push(t)
	    input_val+=1
	    a=Input[input_val]
	  elif run.LR_action[s][value(a)][0][0]=='r':
	    r=0
	    for k in range(1,len(run.LR_action[s][value(a)][0])):
	      r=r*10+int(run.LR_action[s][value(a)][0][k])
	    print "reduce by<b>", code.rules[r][0]," -> ",
	    for i in range(1,len(code.rules[r])):
	      print code.rules[r][i],
	    print "</b>"
	    b=len(code.rules[r])-1
	    for i in range(0,b):
	      tmp=S.pop()
	    t=S.top()
	    A=code.rules[r][0]
	    for g in run.LR_goto:
	      if g[0]==t and g[1]==A:
		top=g[2]
		break
	    S.push(top)
	  elif run.LR_action[s][value(a)][0][0]=='a':
	    print "accept"
	    break
	  else:
	    print "Error"
	    break
	  print "</td>\n"
	  print "</tr>\n"
	    
	print "</table></a>"
print "</div>"
print "<BR><BR><BR>"
