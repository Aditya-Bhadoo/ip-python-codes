class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def __str__(self):
		return '('+str(self.x)+","+str(self.y)+")"

class Rectangle:
	def __init__(self,Pt1,Pt2):
		if(Pt1.x<Pt2.x and Pt1.y<Pt2.y):
			self.BLpoint=Pt1
			self.TRpoint=Pt2
		elif(Pt2.x<Pt1.x and Pt2.y<Pt1.y):
			self.BLpoint=Pt2
			self.TRpoint=Pt1
		elif(Pt1.x<Pt2.x and Pt1.y>Pt2.y):
			self.BLpoint=Point(Pt1.x,Pt2.y)
			self.TRpoint=Point(Pt2.x,Pt1.y)
		elif(Pt2.x<Pt1.x and Pt2.y>Pt1.y):
			self.BLpoint=Point(Pt2.x,Pt1.y)
			self.TRpoint=Point(Pt1.x,Pt2.y)
	def __str__(self):
		return "("+"("+str(self.BLpoint.x)+","+str(self.BLpoint.y)+")"+"("+str(self.TRpoint.x)+","+str(self.TRpoint.y)+")"+")"

	def __add__(self,rec):
		minx=min(self.BLpoint.x,rec.BLpoint.x,self.TRpoint.x,rec.TRpoint.x)
		miny=min(self.BLpoint.y,rec.BLpoint.y,self.TRpoint.y,rec.TRpoint.y)
		maxx=max(self.BLpoint.x,rec.BLpoint.x,self.TRpoint.x,rec.TRpoint.x)
		maxy=max(self.BLpoint.y,rec.BLpoint.y,self.TRpoint.y,rec.TRpoint.y)
		return Rectangle(Point(minx,miny),Point(maxx,maxy))
	def __lt__(self,A):
		if(self.BLpoint.x>A.BLpoint.x):
			return False
		if(self.BLpoint.x<A.BLpoint.x):
			return True


if __name__ == '__main__':
	l=[int(i) for i in input().split()]
	p1=Point(l[0],l[1])
	
	l=[int(i) for i in input().split()]
	p2=Point(l[0],l[1])

	R1=Rectangle(p1,p2)
	print(R1)

	l=[int(i) for i in input().split()]
	p3=Point(l[0],l[1])

	l=[int(i) for i in input().split()]
	p4=Point(l[0],l[1])

	R2=Rectangle(p3,p4)
	print(R2)

	R3=R1+R2
	print(R3)
	L=[R1,R2,R3]
	L.sort()
	for i in L:
		print(i)

