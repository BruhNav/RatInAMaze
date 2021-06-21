import MazeMaps 

mat = [
	[1,0,0,1,1,2],
	[1,0,0,1,0,0],
	[1,1,1,1,0,0],
	[0,0,1,0,0,0],
	[0,0,1,1,1,0],
	[0,1,1,0,0,0]
	]

def printans(mat):

	for i in mat:
		for j in i:
			print(j,end="")
		print("")

#this fuction tells if the specified cell is safe to go 

def isSafe(posY,posX,mat):
	
	if (mat[posY][posX]==1 and posY<6 and posY>=0 and posX<6 and posX>=0 ):
		return True
	return False

#this fuction tells if the mouse has reached the wrong path and has to backtrack his path
#if the mouse has only one of the four direction left to move which is the direcion he came from

def noWay(posY,posX,mat):

	d=isSafe(posY+1,posX,mat)
	u=isSafe(posY-1,posX,mat)
	l=isSafe(posY,posX-1,mat)
	r=isSafe(posY,posX+1,mat)


	if(
	(l==False and r==False and u==False and d==True) or 
	(l==False and r==False and u==True and d==False) or 
	(l==False and r==True and u==False and d==False) or 
	(l==True and r==False and u==False and d==False)
	):
		return True
	


solMat=[[0 for j in range(6)]for i in range(6)]

solMat[0][0]=1

posY=0
posX=0

while mat[posY][posX]!=2:

	print(posX,posY)

	if isSafe(posY-1,posX,mat):
		solMat[posY-1][posX] = 1
		posY=posY-1
		
		if noWay(posY,posX,mat) and posY>0 and posX>0:
			solMat[posY][posX]=0

			posY=posY+1

	if isSafe(posY+1,posX,mat): 
		solMat[posY+1][posX] = 1
		posY=posY+1
		
		if noWay(posY,posX,mat) and posY>0 and posX>0:
			solMat[posY][posX]=0

			posY=posY-1

	if isSafe(posY,posX-1,mat):
		solMat[posY][posX-1] = 1
		posX=posX-1

		if noWay(posY,posX,mat) and posY>0 and posX>0:
			solMat[posY][posX]=0

			posX=posX+1

	if isSafe(posY,posX+1,mat):
		solMat[posY][posX+1] = 1
		posX=posX+1

		if noWay(posY,posX,mat) and posY>0 and posX>0:
			solMat[posY][posX]=0

			posX=posX-1

	printans(solMat)
	


printans(solMat)


		

		

		
