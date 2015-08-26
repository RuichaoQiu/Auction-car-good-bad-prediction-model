import csv
import math

class TNode(object):
	def __init__(self):
		self.d = []
		self.tot = 0
		self.posi = 0
		self.nega = 0
		self.v = []
		self.left = None
		self.right = None
		self.res = "2"
		self.index = 0

	def calcCount(self):
		self.tot = len(self.d)
		for item in self.d:
			if item[0] == '0':
				self.nega += 1
			else:
				self.posi += 1

def info(x,y):
	if x == 0 or y == 0:
		return 0.0
	tmp1 = float(x)/float(x+y)
	tmp2 = float(y)/float(x+y)
	return -tmp1*math.log(tmp1)/math.log(2)-tmp2*math.log(tmp2)/math.log(2)

def doit(node):
	node.calcCount()
	if node.tot == node.posi:
		node.res = "1"
		return
	if node.tot == node.nega:
		node.res = "0"
		return
	t = [[0 for si in range(2)] for sj in range(2)]
	mini = 10.0
	mininum = 0
	for i in range(1,len(node.v)):
		if node.v[i] == False:
			t[0][0] = 0
			t[0][1] = 0
			t[1][0] = 0
			t[1][1] = 0
			for item in node.d:
				if item[i] == "0":
					if item[0] == "0":
						t[0][0] += 1
					else:
						t[0][1] += 1
				else:
					if item[0] == "0":
						t[1][0] += 1
					else:
						t[1][1] += 1
			infoa = float(t[0][0]+t[0][1])/float(t[0][0]+t[0][1]+t[1][0]+t[1][1])*info(t[0][0],t[0][1])
			infoa += float(t[1][0]+t[1][1])/float(t[0][0]+t[0][1]+t[1][0]+t[1][1])*info(t[1][0],t[1][1])
			if infoa < mini:
				mini = infoa
				mininum = i
	node.index = mininum
	node.left = TNode()
	node.right = TNode()

	for item in node.d:
		if item[mininum] == "0":
			node.left.d.append(item)
		else:
			node.right.d.append(item)
	node.left.v = node.v[:]
	node.right.v = node.v[:]
	node.left.v[mininum] = True
	node.right.v[mininum] = True
	doit(node.left)
	doit(node.right)

def dotest(it):
	
	cur = root
	while cur.res == "2":
		if it[cur.index-1] == "0":
			cur = cur.left
		else:
			cur = cur.right
	return cur.res


root = TNode()

with open('newtrain.csv', 'rb') as f:
	reader = csv.reader(f)
	data = list(reader)

for i in range(len(data)):
	root.d.append(data[i])
root.v = [False for sk in range(len(root.d[1]))]

doit(root)
dtest = []
with open('newtest.csv', 'rb') as f:
	reader = csv.reader(f)
	dtest = list(reader)



with open('id.csv', 'rb') as f:
	reader = csv.reader(f)
	listid = list(reader)


with open('res.csv', 'w') as csvfile:
	fieldnames = ['RefId', 'IsBadBuy']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for j in range(1,len(dtest)):
		writer.writerow({'RefId': listid[j][0], 'IsBadBuy': dotest(dtest[j])})




