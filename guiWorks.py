# import pygame module in this program
import pygame
import random
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
white = (255, 255, 255)

X = 600
Y = 600

display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('rat in a maze')

bkgr_image = pygame.image.load(r'D:\demo\pyprograms\GUIwork\576.jpg')

blockage1= pygame.image.load(r'D:\demo\pyprograms\GUIwork\rock.png')
blockage2= pygame.image.load(r'D:\demo\pyprograms\GUIwork\rock2.png')
blockage3= pygame.image.load(r'D:\demo\pyprograms\GUIwork\rock3.png')

blockages=[blockage1,blockage2,blockage3]
character = pygame.image.load(r'D:\demo\pyprograms\GUIwork\character.png')

while True :

	display_surface.fill(white)

	# copying the image surface object
	# to the display surface object at
	# (0, 0) coordinate.
	display_surface.blit(bkgr_image, (0, 0))

	for i in range(60):
		randomobsticle=random.choice(blockages)
		display_surface.blit(bkgr_image,(0,0))
		display_surface.blit(character,(i*5,0))
		pygame.display.update()
		pygame.time.delay(100)


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
			
