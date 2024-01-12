#Shiyam Vasanthan 

import random
import pygame
import math 

pygame.init()

#Set up the window size, title, and fill it with a white background
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Slides and Ladders 8 by 9')
window.fill((255, 255, 255))

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 204, 0)
green = (102, 204, 0)

#Width of one tile on the grid
width = 50

#Number font
arial = pygame.font.SysFont('Arial Bold', 25)

#Draw number counter
counter = 0

#Switch direction of draw number counter every row
switch_row = False

#Switch between red and blue cpu characters
red_cpu = True

#Red and blue characters x and y coordinates
red_x = 25
red_y = 475
blue_x = 75
blue_y = 475

#Red and blue position
red_pos = 0
blue_pos = 0

#Draw grid using nested for loops
for y in range(9):
	for x in range(8):
		pygame.draw.rect(window, black, (x * width + 1, y * width + 1, width, width), 2)
	
#Draw numbers in an alternating pattern every row
for j in range(9):
	for i in range(1, 9):
		counter += 1
		numbers = arial.render(str(counter), False, black)
		if switch_row == False:
			window.blit(numbers,((i - 1) * 50 + 4, 400 - (j * 50) + 3))
		else:
			window.blit(numbers,(350 - (i - 1) * 50 + 4, 400 - (j * 50) + 3))
			
	#Switch the direction of the number counter every row
	if switch_row == False:
		switch_row = True
	else:
		switch_row = False

#Draw ladder function
#Length is the number of steps on the ladder minus 1
#When the ladder goes from left to right get the start and end x, y coordinates for the left side rail
#When the ladder goes from right to left get the start and end x, y coordinates for the right side rail
def ladder(start_x, start_y, end_x, end_y, length):	
	#Calculate the rise and run of the ladder
	run = (end_x - start_x)/length
	rise = (end_y - start_y)/length
	
	#Calculate the slope of the ladder using rise over run
	slope = rise/run
	
	#Draw the left/right side rail
	pygame.draw.line(window, yellow, (start_x, start_y), (end_x, end_y), 5)
	
	#When the ladder goes from left to right (In python its negative slope because origin is at lop left corner instead of bottom left)
	if slope < 0:
		#Draw the ladder steps
		for i in range(1, length):			
			pygame.draw.line(window, yellow, (start_x + run*i, start_y + rise*i), ((start_x + 10) + run*i, (start_y + 10) + rise*i), 5)

		#Draw the right side rail
		pygame.draw.line(window, yellow, (start_x + 10, start_y + 10), (end_x + 10, end_y + 10), 5)
		
	#When the ladder goes from right to left (In python its positive slope because origin is at lop left corner instead of bottom left) 
	elif slope > 0:
		#Draw the ladder steps
		for i in range(1, length):			
			pygame.draw.line(window, yellow, (start_x + run*i, start_y + rise*i), ((start_x - 10) + run*i, (start_y + 10) + rise*i), 5)

		#Draw the left side rail
		pygame.draw.line(window, yellow, (start_x - 10, start_y + 10), (end_x - 10, end_y + 10), 5)	

#Draw slides
def slide(start_x, start_y, end_x, end_y):
	#Calculate the rise and run of the ladder
	run = (end_x - start_x)
	rise = (end_y - start_y)
	
	#Calculate the slope of the slide using rise over run
	slope = rise/run
	
	#When the slide goes from right to left
	if slope < 0:		
		#Inner part of the slide
		pygame.draw.polygon(window, green, [(start_x, start_y), (end_x, end_y), (end_x + 10, end_y + 10), (start_x + 10, start_y + 10)])
		#Draw the right side of the slide
		pygame.draw.line(window, black, (start_x + 10, start_y + 10), (end_x + 10, end_y + 10), 5)
		
	#When the slide goes from right to left
	elif slope > 0:
		#Inner part of the slide
		pygame.draw.polygon(window, green, [(start_x, start_y), (end_x, end_y), (end_x - 10, end_y + 10), (start_x - 10, start_y + 10)])
		#Draw the left side of the slide
		pygame.draw.line(window, black, (start_x - 10, start_y + 10), (end_x - 10, end_y + 10), 5)	

	#Draw the left/right side of slide
	pygame.draw.line(window, black, (start_x, start_y), (end_x, end_y), 5)

#Call the ladder and slide functions in between so that they don't get cleared off the screen
def ladder_slide():
	#Draw the slides by calling the function
	#Slide number 16 to 2
	slide(95, 405, 45, 375)
	#Slide number 29 to 5
	slide(240, 415, 190, 275)
	#Slide number 34 to 17
	slide(25, 325, 75, 225)
	#Slide number 42 to 25
	slide(395, 260, 340, 175)
	#Slide number 46 to 36
	slide(198, 202, 145, 175)
	#Slide number 68 to 63
	slide(75, 75, 160, 30)
	#Slide number 70 to 53
	slide(225, 125, 260, 30)

	#Create ladders by calling the ladder function
	#Ladder number 7 to 24
	ladder(325, 425, 355, 330, 5)
	#Ladder number 14 to 31
	ladder(143, 365, 95, 280, 5)
	#Ladder number 22 to 52
	ladder(295, 315, 195, 130, 10)
	#Ladder number 41 to 59
	ladder(397, 161, 295, 80, 6)
	#Ladder number 47 to 61
	ladder(75, 160, 155, 80, 6)
	#Ladder number 49 to 65
	ladder(24, 125, 37, 33, 4)
	
#Draw the ladders and slides at the beginning of the game
ladder_slide()

#Draw the red and blue character at the beginning
pygame.draw.circle(window, red, (25, 475), 10, 0)
pygame.draw.circle(window, blue, (75, 475), 10, 0)
pygame.display.update()
pygame.time.delay(1000)

#Main Game While Loop
while True:	
	#Randomly roll dice
	dice = random.randint(1, 6)
		
	#Change the position of the red or blue character based on the dice number
	if red_cpu == True:
		red_pos += dice	
	else:
		blue_pos += dice
		
	#Clear the screen to refresh dice and text right above dice
	pygame.draw.rect(window, white, (428, 378, width - 6, width - 6), 0)
	pygame.draw.rect(window, white, (410, 353, 80, 15), 0)
	
	#Switch the cpu character each time the dice is rolled
	if red_cpu == False:
		red_cpu = True
		turn = arial.render("Blue Turn", False, blue)
		window.blit(turn,(410, 353))
	else:
		red_cpu = False
		turn = arial.render("Red Turn", False, red)
		window.blit(turn,(413, 353))
	
	#Clear the previous position of the red and blue cpu
	if red_pos > 0:
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
	
	if blue_pos > 0:
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
	
	#Draw the ladders and slides so they don't get cleared by the red and blue cpu
	ladder_slide()
	
	#Dice square outline
	pygame.draw.rect(window, black, (425, 375, width, width), 3)
	
	#Change the number of circles to represent the different dice numbers
	if dice == 1:
		pygame.draw.circle(window, black, (450, 400), 5, 0)
	elif dice == 2:
		pygame.draw.circle(window, black, (450 - 50/4, 400 - 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 + 50/4), 5, 0)
	elif dice == 3:
		pygame.draw.circle(window, black, (450, 400), 5, 0)
		pygame.draw.circle(window, black, (450 - 50/4, 400 - 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 + 50/4), 5, 0)
	elif dice == 4:
		pygame.draw.circle(window, black, (450 - 50/4, 400 - 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 + 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 - 50/4, 400 + 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 - 50/4), 5, 0)
	elif dice == 5:
		pygame.draw.circle(window, black, (450, 400), 5, 0)
		pygame.draw.circle(window, black, (450 - 50/4, 400 - 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 + 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 - 50/4, 400 + 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 - 50/4), 5, 0)
	elif dice == 6:
		pygame.draw.circle(window, black, (450 - 50/4, 400 - 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 + 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 - 50/4, 400 + 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400 - 50/4), 5, 0)
		pygame.draw.circle(window, black, (450 - 50/4, 400), 5, 0)
		pygame.draw.circle(window, black, (450 + 50/4, 400), 5, 0)
	
	#Calculate the position of the red cpu using the modulus function to help me calculate the coordinates corresponding to each position on the grid
	if (red_pos >= 1 and red_pos <= 8):
		red_x = (red_pos * 50) - 25
		red_y = 425
	elif (red_pos >= 9 and red_pos <= 16):
		red_x = 375 - (red_pos%9 * 50)
		red_y = 375
	elif (red_pos >= 17 and red_pos <= 24):
		red_x = (red_pos%16 * 50) - 25
		red_y = 325
	elif (red_pos >= 25 and red_pos <= 32):
		red_x = 375 - (red_pos%25 * 50)
		red_y = 275
	elif (red_pos >= 33 and red_pos <= 40):
		red_x = (red_pos%32 * 50) - 25
		red_y = 225
	elif (red_pos >= 41 and red_pos <= 48):
		red_x = 375 - (red_pos%41 * 50)
		red_y = 175
	elif (red_pos >= 49 and red_pos <= 56):
		red_x = (red_pos%48 * 50) - 25
		red_y = 125
	elif (red_pos >= 57 and red_pos <= 64):
		red_x = 375 - (red_pos%57 * 50)
		red_y = 75
	elif (red_pos >= 65 and red_pos <= 71):
		red_x = (red_pos%64 * 50) - 25
		red_y = 25
	elif (red_pos >= 72):
		red_x = 375
		red_y = 25
		
	#Calculate the position of the blue cpu using the modulus function to help me calculate the coordinates corresponding to each position on the grid
	if (blue_pos >= 1 and blue_pos <= 8):
		blue_x = (blue_pos * 50) - 25
		blue_y = 425
	elif (blue_pos >= 9 and blue_pos <= 16):
		blue_x = 375 - (blue_pos%9 * 50)
		blue_y = 375
	elif (blue_pos >= 17 and blue_pos <= 24):
		blue_x = (blue_pos%16 * 50) - 25
		blue_y = 325
	elif (blue_pos >= 25 and blue_pos <= 32):
		blue_x = 375 - (blue_pos%25 * 50)
		blue_y = 275
	elif (blue_pos >= 33 and blue_pos <= 40):
		blue_x = (blue_pos%32 * 50) - 25
		blue_y = 225
	elif (blue_pos >= 41 and blue_pos <= 48):
		blue_x = 375 - (blue_pos%41 * 50)
		blue_y = 175
	elif (blue_pos >= 49 and blue_pos <= 56):
		blue_x = (blue_pos%48 * 50) - 25
		blue_y = 125
	elif (blue_pos >= 57 and blue_pos <= 64):
		blue_x = 375 - (blue_pos%57 * 50)
		blue_y = 75
	elif (blue_pos >= 65 and blue_pos <= 71):
		blue_x = (blue_pos%64 * 50) - 25
		blue_y = 25
	elif (blue_pos >= 72):
		blue_x = 375
		blue_y = 25
		
	#Update the display so the game piece moves on the board
	pygame.draw.circle(window, red, (red_x, red_y), 10, 0)
	pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	pygame.display.update()
	
	#If the red or the blue cpu land on ladder 7, go to 24
	if red_pos == 7:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 24
		red_x = (red_pos%16 * 50) - 25
		red_y = 325
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 7:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 24
		blue_x = (blue_pos%16 * 50) - 25
		blue_y = 325
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on ladder 14, go to 31
	elif red_pos == 14:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 31
		red_x = 375 - (red_pos%25 * 50)
		red_y = 275
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 14:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 31
		blue_x = 375 - (blue_pos%25 * 50)
		blue_y = 275
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)		
	#If the red or the blue cpu land on slide 16, go to 2
	elif red_pos == 16:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 2
		red_x = (red_pos * 50) - 25
		red_y = 425
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 16:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 2
		blue_x = (blue_pos * 50) - 25
		blue_y = 425
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)	
	#If the red or the blue cpu land on ladder 22, go to 52
	elif red_pos == 22:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 52
		red_x = (red_pos%48 * 50) - 25
		red_y = 125
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 22:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 52
		blue_x = (blue_pos%48 * 50) - 25
		blue_y = 125
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on ladder 29, go to 5
	elif red_pos == 29:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 5
		red_x = (red_pos * 50) - 25
		red_y = 425
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 29:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 5
		blue_x = (blue_pos * 50) - 25
		blue_y = 425
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on slide 34, go to 17
	elif red_pos == 34:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 17
		red_x = (red_pos%16 * 50) - 25
		red_y = 325
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 34:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 17
		blue_x = (blue_pos%16 * 50) - 25
		blue_y = 325
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on slide 41, go to 59
	elif red_pos == 41:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 59
		red_x = 375 - (red_pos%57 * 50)
		red_y = 75
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 41:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 59
		blue_x = 375 - (blue_pos%57 * 50)
		blue_y = 75
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on slide 42, go to 25
	elif red_pos == 42:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 25
		red_x = 375 - (red_pos%25 * 50)
		red_y = 275
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 42:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 25
		blue_x = 375 - (blue_pos%25 * 50)
		blue_y = 275
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on slide 46, go to 36
	elif red_pos == 46:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 36
		red_x = (red_pos%32 * 50) - 25
		red_y = 225
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 46:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 36
		blue_x = (blue_pos%32 * 50) - 25
		blue_y = 225
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on ladder 47, go to 61
	elif red_pos == 47:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 61
		red_x = 375 - (red_pos%57 * 50)
		red_y = 75
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 47:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 61
		blue_x = 375 - (blue_pos%57 * 50)
		blue_y = 75
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on ladder 49, go to 65
	elif red_pos == 49:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 65
		red_x = (red_pos%64 * 50) - 25
		red_y = 25
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 49:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 65
		blue_x = (blue_pos%64 * 50) - 25
		blue_y = 25
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on slide 68, go to 63
	elif red_pos == 68:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 63
		red_x = 375 - (red_pos%57 * 50)
		red_y = 75
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 68:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 63
		blue_x = 375 - (blue_pos%57 * 50)
		blue_y = 75
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	#If the red or the blue cpu land on slide 70, go to 53
	elif red_pos == 70:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (red_x, red_y), 10, 0)
		red_pos = 53
		red_x = (red_pos%48 * 50) - 25
		red_y = 125
		pygame.draw.circle(window, red, (red_x, red_y), 10, 0)			
	elif blue_pos == 70:
		pygame.time.delay(500)
		pygame.draw.circle(window, white, (blue_x, blue_y), 10, 0)
		blue_pos = 53
		blue_x = (blue_pos%48 * 50) - 25
		blue_y = 125
		pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
		
	#Draw the ladders and slides so they don't clear when the red and blue cpu's climb up the ladder or slide down
	ladder_slide()
	
	#Redraw the red and blue cpu to avoid the ladder and slides been drawn over
	pygame.draw.circle(window, red, (red_x, red_y), 10, 0)
	pygame.draw.circle(window, blue, (blue_x, blue_y), 10, 0)
	
	#Change turns every half a second
	pygame.display.update()
	pygame.time.delay(500)
	
	#End the game if somebody wins
	if (red_pos >= 72):
		winner = arial.render("Red Wins!", False, red)
		window.blit(winner, (408, 20))
		break
	elif (blue_pos >= 72):
		winner = arial.render("Blue Wins!", False, blue)
		window.blit(winner, (405, 20))
		break
	

#Display the result at the end for 2 seconds then terminate
pygame.display.update()
pygame.time.delay(2000)	
