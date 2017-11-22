from StudentRecord import *

def readrecords(filen):
	lines=open(filen).read().splitlines()
	slist=[]
	for s in lines:
		c=s.split(" ")
		slist.append(Student(c[0],c[1],c[2],c[3],c[4]))
	return slist

def order_records(l):
	l=sorted(l)
	return l

def display_ordered_data(ordl):
	for i in ordl:
		print(i.Rollnumber,i.FirstName,i.LastName,i.Program,i.CGPA)

if __name__ == '__main__':
	l=readrecords("studentdata.txt")
	display_ordered_data(order_records(l))
