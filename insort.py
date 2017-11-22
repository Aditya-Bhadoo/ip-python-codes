def insort(l):
	for i in range(1,len(l)):
		j=i-1
		while(j>=0 and l[j+1]<=l[j]):
			l[j+1],l[j]=l[j],l[j+1]
			j-=1
			print(l)
			print(i,j+1)



if __name__ == '__main__':
	l=[10,8,19,0,-6,6]
	print(l)
	insort(l)


