'''
Aditya Bhadoo
2017008
B4
'''

import math
import copy
import dijkstra

connections=[]
weights=[]

def graph():
	global connections,weights
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


def asc_weight(v):
	global weights,connections
	wht=weights[v]
	con=sorted(connections[v])
	return con



def bfs(graph,source):
	global ncompl,dist
	connections=graph[0]							#checked
	weights=graph[1]
	
	visited=[source]								#initialising visited
	queue=[source]									#initialising queue

	while(len(queue)!=0):
		vertex=queue[0]
		del queue[0]

		for icon in range(len(connections[vertex])):
			con=connections[vertex][icon]				#variable that takes the values of the connections to the vertex
			con_list=asc_weight(vertex)
			w=con_list[icon]
			if(w not in visited):
				queue.append(w)
				visited.append(w)
	wikichu=[]
	shar=dijkstra.dijkstra(graph,source)
	for i in visited:
		wikichu.append(shar[i])
	return visited,wikichu

			


if __name__ == '__main__':
	print(bfs(graph(),0))