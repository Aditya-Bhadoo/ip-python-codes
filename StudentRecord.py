class Student:
	def __init__(self,R,F,L,P,CG):
		self.Rollnumber=R
		self.FirstName=F
		self.LastName=L
		self.Program=P
		self.CGPA=float(CG)

	def __cmp__(self,A):
		if(int(self.Rollnumber[0:4])>int(A.Rollnumber[0:4])):
			return 1
		if(int(self.Rollnumber[0:4])<int(A.Rollnumber[0:4])):
			return -1
		if(self.Program>A.Program):
			return 1
		if(self.Program<A.Program):
			return -1
		if(self.CGPA>A.CGPA):
			return -1
		if(self.CGPA<A.CGPA):
			return 1
	def comes_before(self,other):
		if(self>other):
			return True
		else:
			return False
	


