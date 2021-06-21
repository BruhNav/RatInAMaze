import MazeMaps

mat = MazeMaps.mapit()


	


def isSafe(posX,posY,mat,n):
	
	if (mat[posX][posY]==1 and posX<n and posX>=0 and posY<n and posY>=0 ):
		return True
	
cellTraveld = []





def solveMaze( mat ):

    solMat = [ [ 0 for j in range(6) ] for i in range(6) ]
     
    if movingCode( 0, 0,mat, solMat) == False:
        print("Solution doesn't exist")
        return False
     
    printSolution(solMat)
    return True


def printSolution( sol ):
     
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        print("")

def movingCode(mat,posX,posY,solMat):

	if mat[posX][posY]==2:
		solMat[posX][posY]=1
		return True

	if isSafe(posX,posY,mat,6) == True:

		cellTraveld.append((posX,posY))

		if solMat[posX][posY] == 1:

			return False


		solMat[posX][posY]=1

		#output posX and posY to light up in grid


		if movingCode(mat,posX+1,posY,solMat)==1:
			
			return True

		if movingCode(mat,posX-1,posY,solMat)==1:
			
			return True

		if movingCode(mat,posX,posY+1,solMat):
			
			return True

		if movingCode(mat,posX,posY-1,solMat)==1:

			return True
		

		if movingCode(mat,posX,posY,solMat)==0:

			return False


	
		 




if __name__=="__main__":
	solveMaze(mat)


	



	






# n =int( input("Dimension: "))

# mat = [[0]*n]*n
# print(mat)