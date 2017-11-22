stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

def corr_stock():
	global stock
	a=False
	for i in stock:
		if(stock[i]>0):
			a=True
	return a

def bill(p):
	global stock
	s=0
	for i in p:
		if(stock[i]>0):
			s+=p[i]
			stock[i]-=1
	return s

if __name__ == '__main__':
	prices={"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
	while(corr_stock()):
			print(bill(prices))
			print(stock)