'''
Aditya Bhadoo
2017008
B4
'''
import math
import copy

connections=[]
weights=[]
ncompl=[]
dist=[]

def graph():

	v=int(input())
	connections=[]
	weights=[]

	
	for i in range(v):
		c=int(input())
		a=[]
		b=[]
		for k in range(c):
			s=[int(x) for x in input().split(" ")]
			a.extend([s[0]])
			b.extend([s[1]])
		connections.append(a)
		weights.append(b)
	return(connections,weights)



def corr_ncompl():
	global ncompl
	a=False
	for x in ncompl:
		if(dist[x]!=math.inf):
			a=True
	return a

def corr_min_dist():								#checked
	global ncompl,dist
	m=math.inf
	for x in ncompl:
		if(dist[x]<m):
			m=dist[x]
	return(dist.index(m))

def dijkstra(graph,source):
	global ncompl,dist
	connections=graph[0]							#checked
	weights=graph[1]
	
	ncompl=[x for x in range(len(weights))]
	dist=[x for x in range(len(weights))]
	
	#forming th dist list
	dist[source]=0
	for x in range(len(connections)):
		if(x!=source):
			dist[x]=math.inf


	while((len(ncompl)!=0) and corr_ncompl()):
		vertex=corr_min_dist()
		
		try:
			del ncompl[ncompl.index(vertex)]
		except ValueError:						#this ValueError occurs only when vertex is not in ncompl
			amz=dist[vertex]
			dist[vertex]=math.inf				#So, the corr_min_dist() fill work completely fine even when we change the value of dist[vertex] to inf
			new=corr_min_dist()
			dist[vertex]=amz
			vertex=new
			del ncompl[ncompl.index(vertex)]

		for icon in range(len(connections[vertex])):
			con=connections[vertex][icon]				#variable that takes the values of the connections to the vertex
			tot=dist[vertex] + weights[vertex][icon]	#total distance from the vertex
			if(tot<dist[con]):
				dist[con]=tot
	return dist

if __name__ == '__main__':
	print(dijkstra(graph(),0))

