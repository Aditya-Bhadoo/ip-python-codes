'''
x=int(input())
n=int(input())
p=1
for i in range(n):
	p*=x
print(p)
'''
def recxn(x,n):
	if(n==0):
		return 1
	else:
		return recxn(x,n-1)*x
if __name__ == '__main__':
	print(recxn(4,-1))