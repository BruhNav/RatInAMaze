import MazeMaps

def blockagepoints(m):

	block=[]

	x=0
	y=0

	for i in m :
		
		for j in i:
			
			if j==0:
				block.append((x*50,y*50))
			x=x+1
			x=x%10
		y=y+1

	return block
