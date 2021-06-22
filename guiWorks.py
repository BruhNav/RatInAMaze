# import pygame module in this program
import pygame
import random
import time
import maze
import MazeMaps
import BlockageDetector

m = MazeMaps.mapit()
n = len(m)


navigator = maze.printPath(m,n)



pygame.init()
white = (255, 255, 255)

X = 500
Y = 500 

display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('rat in a maze')

bkgr_image = pygame.image.load(r'C:\Users\Pranav\Desktop\ITW Backup\Backgrounds\RockyBackground.jpg')

blockage1= pygame.image.load(r'C:\Users\Pranav\Desktop\ITW Backup\Icons\grass blockage.jpg')

character = pygame.image.load(r'C:\Users\Pranav\Desktop\ITW Backup\Icons\character.png')

while True :

	display_surface.fill(white)

	# copying the image surface object
	# to the display surface object at
	# (0, 0) coordinate.
	display_surface.blit(bkgr_image, (0, 0))

	for i in BlockageDetector.blockagepoints(m):
		display_surface.blit(blockage1,i)
		


	# iterate over the list of Event objects
	# that was returned by pygame.event.get() method.
	for event in pygame.event.get() :

		# if event object type is QUIT
		# then quitting the pygame
		# and program both.
		if event.type == pygame.QUIT :

			# deactivates the pygame library
			pygame.quit()

			# quit the program.
			quit()

		# Draws the surface object to the screen.
		pygame.display.update()
			


#for i in range(60):
# 		display_surface.blit(bkgr_image,(0,0))
# 		display_surface.blit(character,(i*5,0))
# 		pygame.display.update()
# 		pygame.time.delay(100)