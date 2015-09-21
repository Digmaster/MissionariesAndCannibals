from copy import deepcopy as copy

def arrSub(vec1, vec2):
	for i in range(len(vec1)):
		vec1[i] = vec1[i]-vec2[i]
	return vec1

def arrAdd(vec1, vec2):
	for i in range(len(vec1)):
		vec1[i] = vec1[i]+vec2[i]
	
	return vec1

def checkWin(vec):
	if(vec[0]==0 and vec[1]==0):
		return True
	return False

def checkLoss(vec):
	if(vec[0]!=0 and vec[0]<vec[1]):
		return True
	if(vec[0]!=3 and vec[0]>vec[1]):
		return True
	return False

def checkArray(vec):
	if(vec[0] > 3 or vec[1] > 3 or vec[2] > 1 or vec[0] < 0 or vec[1] < 0 or vec[2] < 0):
		return False
	return True

def sumArray(vec):
	s = 0
	for i in vec:
		s + i
	return i

def printArray(vec):
	return "<{0},{1},{2}>".format(vec[0],vec[1],vec[2])

def getMoves():
	a = []
	a.append([1,0,1])
	a.append([0,1,1])
	a.append([1,1,1])
	a.append([2,0,1])
	a.append([0,2,1])
	return a



def recurse(states, num):

	n = []
	m = {}
	oldNum = num
	for i in states:
		for move in getMoves():
			c = copy(i)
			if(c[2]==1):
				arrSub(c, move)
			else:
				arrAdd(c, move)
			if(not checkArray(c)):
				continue
			if(checkLoss(c)):
				continue
			num = num+1
			if(checkWin(c)):
				return [[i, move,oldNum],[[0,0,0],[0,0,0],num]]
			m[printArray(c)] = [i, move, num]
			n.append(c)

	v = recurse(n, num)
	if(v!=False):
		v.insert(0, m[printArray(v[0][0])])
		return v
	return False

print "Algorithm: Depth first search"
v = recurse([[3,3,1]], 0)
for i in v:
	print("{0}, {1}, {2}".format(printArray(i[0]),printArray(i[1]),i[2]))