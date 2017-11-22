def swapRow(A,row1,row2):
	l=len(A)-1
	assert((row1<=l) and (row2<=l)),"enter valid rows to swap"
	x=A[row1]
	A[row1]=A[row2]
	A[row2]=x

def Row_Transformation(A,x,row1,row2):
	l=len(A)-1
	assert((row1<=l) and (row2<=l)),"enter valid rows to transform"
	for i in range(len(A[0])):
		A[row2][i]=A[row2][i]+x*A[row1][i]

def negatedown(A,row1,col):
	a=A[row1][col]
	for i in range(row1,len(A)):
		if(i==row1):
			continue
		store=A[i][col]
		x=-store/a
		Row_Transformation(A,x,row1,i)


def col_down(row,col):						#performs necessary operations on the column downwards
	t=False
	while(t==False):
		if(A[row][col]==0):
			if(row==(len(A)-1)):
				t=True
				break
			else:
				nz_row=-50
				for i in range((row+1),(len(A))):

					if(A[i][col]!=0):
						nz_row=i
						swapRow(A,row,nz_row)
						t=True
						break
				if(nz_row==-50):
					break
		if(A[row][col]!=0):
			t=True
			negatedown(A,row,col)
			break
			
	return t

def count(A):
	rank=0
	r0=[0 for x in range(len(A[0]))]
	for row in A:
		if(row!=r0):
			rank+=1
	return rank

def MatrixRank(A):
	row=0
	col=0
	nrows=len(A)-1
	ncols=len(A[0])-1
	while(row<=nrows and col<=ncols):
		if(col_down(row,col)):
			row+=1
			col+=1
		else:
			col+=1
	
	return count(A)


if __name__ == '__main__':
	A=[]
	for x in range(int(input())):
		l=[int(i) for i in input().split(",")]
		A.append(l)


	print(MatrixRank(A))
	for i in A:
		print(i)
	