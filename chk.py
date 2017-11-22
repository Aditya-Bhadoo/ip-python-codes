class polynomial:

	def __init__(self,l):
		self.pol=l

	def __add__(self,x):

		if(len(self.pol)>=len(x.pol)):
			n1=len(self.pol)
			n2=len(x.pol)
			l1=self.pol
			l2=x.pol
		else:
			n1=len(x.pol)
			n2=len(self.pol)
			l1=x.pol
			l2=self.pol
		
		for i in range(n2):
			l1[i]=l1[i]+l2[i]
		return l1

if __name__ == '__main__':
	ins=polynomial([2,-1,0,1,3])
	print(ins.pol)
	other=polynomial([1,2,3])
	l=other+ins
	print(l)