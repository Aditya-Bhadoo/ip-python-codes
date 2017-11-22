class palin:
	def __init__(self,s):
		self.fadstr=s

	def palindrome(self):
		n=len(self.fadstr)
		ans=0
		for i in range(n//2):
			if(self.fadstr[i]=="."):
				self.fadstr[i]=self.fadstr[i-n]
			if(self.fadstr[i]!=self.fadstr[i-n]):
				ans=-1
				break
		if(ans==-1):
			print(-1)
		else:
			ans=""
			if(self.fadstr[(n+1)//2-1]=="."):
				self.fadstr[(n+1)//2-1]="a"
			for i in self.fadstr:
				ans+=i
			print(ans)

if __name__ == '__main__':
	for i in range(int(input())):
		s=list(input())
		obj=palin(s)
		n=len(obj.fadstr)
		obj.palindrome()
		print(obj.fadstr[(n+1)//2-1])


