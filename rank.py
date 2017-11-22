#member1- Aditya Bhadoo, Roll Number- 2017008
#member2- Divyansh Agarwal, Roll Number- 2017340


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

def negate(A,row1):
	a=A[row1][row1]
	for i in range(len(A)):
		if(i==row1):
			continue
		store=A[i][row1]
		x=-store/a
		Row_Transformation(A,x,row1,i)

def last_col_swap(A,row1):
	n=len(A[0])-1
	for i in range(len(A)):
		x=A[i][row1]
		A[i][row1]=A[i][n]
		A[i][n]=x

def MatrixRank(A):
	rank=len(A[0])
	row1=0;d=0
	while(row1<rank):
		if(A[row1][row1]!=0):
			negate(A,row1)
		elif(A[row1][row1]==0):
			if(row1==(len(A)-1)):
				row1-=1
				rank-=1
			else:
				nz_row=-50
				for i in range((row1+1),(len(A))):

					if(A[i][row1]!=0):
						nz_row=i
						swapRow(A,row1,nz_row)
						row1-=1
						break

				if(nz_row==-50):
					last_col_swap(A,row1)
					row1-=1
					rank-=1

		row1+=1
		d+=1		
		print(d)
		print(A[0])
		print(A[1])
		print(A[2])
		print(A[3])
	return rank

if __name__ == '__main__':
	A=[[1,2,0,-1,1,-10],[1,3,1,1,-1,-9],[2,5,1,0,0,-19],[3,6,0,0,-6,-27],[1,5,3,5,-5,-7]]

	print(MatrixRank(A))
	print(A[0])
	print(A[1])
	print(A[2])
	print(A[3])
