def Invert(G):
	In={}
	v=[]
	val=G.values()
	for c in val:
		v.extend(c)
	v=list(set(v))
	for x in v:
		In[x]=[]

	for i in G:
		for x in G[i]:
			In[x].append(i)
	return In

if __name__ == '__main__':
	G={2:[1,2,3], 3:[1,2]}
	print(Invert(G))