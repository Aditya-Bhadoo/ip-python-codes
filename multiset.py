from copy import *

class Multiset:
	def __init__(self,elements):
		self.data=elements
		self.data.sort()
	def __str__(self):
		return str(self.data)

	def __mul__(self,n):
		l=[]
		ans=[]
		data=[]
		for i in self.data:
			data.append(i)
			if(i not in l):
				l.append(i)

		for i in l:
			for c in range(data.count(i)*n):
				ans.append(i)

		return Multiset(ans)

	def __sub__(self,m):
		ls=[]
		lm=[]
		ans=[]
		datas=[]
		datam=[]
		for i in self.data:
			datas.append(i)
			if(i not in ls):
				ls.append(i)
		for i in m.data:
			datam.append(i)



		for i in ls:
			n=datas.count(i)-datam.count(i)
			if(n>0):
				for c in range(n):
					ans.append(i)

		return Multiset(ans)

	def subset(self,m):
		datas=[]
		datam=[]
		ls=[]
		lm=[]

		for i in self.data:
			datas.append(i)
			if(i not in ls):
				ls.append(i)

		for i in m.data:
			datam.append(i)
			if(i not in lm):
				lm.append(i)

		for i in ls:
			if(datas.count(i)<=datam.count(i)):
				return True
			else:
				return False
		if(datas==[]):
			return True

if __name__ == '__main__':
	M1=Multiset([1,1,2,3,4,4,5])
	M2=Multiset([1,2,3])
	k=2
	M3=M1*k
	print(M3)
	M4=M2*3
	M5=M1*0
	M6=M5*8
	print('M1=' +str(M1))
	print("M2=" + str(M2))






	M7=M3-M4
	M8=M7-M6
	M9=M8-M3
	print(M7)
	print(M8)
	print(M9)

	print(M3.subset(M8))
	print(M9.subset(M8))
	print(M9.subset(M9))





