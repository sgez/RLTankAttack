import pygame, sys, random, time
from pygame.locals import *
import numpy as np
from Water import Water
from Earth import Earth
from Boat import Boat
from Valve import Valve
from Message import Message
from Functions import Functions
from WhosTurn import WhosTurn
import DEFINES as df
#Win7



def main():
	# set up pygame
	f = Functions()
	
	pygame.init()
	mainClock = pygame.time.Clock()
	
	#WATER LEVEL MATRIX --- NUMBER_OF_WATERS x HEIGHT_OF_WATER
	WATER_LEVEL = df.WATER_LEVEL
	BOATS_ARRAY = np.array([np.invert(WATER_LEVEL), np.invert(WATER_LEVEL)], dtype=bool)
	BOATS_ARRAY[0][1][6] = 1 #position boat_0 to the left
	BOATS_ARRAY[1][3][len(WATER_LEVEL[0])-1] = 1 #position boat_1 to the right
	### Code below makes all values of subarray 0 to 0 --> False
	#BOATS_ARRAY[0][:,:][:,:] = 0 #position boat_0 to the left
	### It will be used to clear the array before filling it with boats coords like this:
	# boats[1].draw_boat(BOATS_ARRAY[1])
	### the above attribute sets boats coordinates based on the array 
	###
	
	print WATER_LEVEL
	print "==="
	print BOATS_ARRAY[0]
	print "==="
	print BOATS_ARRAY[1]
	'''
	exit()
	'''
    #BOAT_ROW[0] SHOWS WHERE BOAT 0 IS
	
	HEIGHT_OF_WATER = len(WATER_LEVEL)
	NUMBER_OF_WATERS = len(WATER_LEVEL[0])
	################################
	
	#exit()
	
	################################
	
	#PARAMS
	IMAGE_WIDTH_HEIGHT = df.IMAGE_WIDTH_HEIGHT 
	IMAGE_HEIGHT = df.IMAGE_HEIGHT
	TOP = df.TOP
	BOTTOM = HEIGHT_OF_WATER * IMAGE_HEIGHT + TOP
	STEP = IMAGE_WIDTH_HEIGHT
	STEPy = IMAGE_HEIGHT
	LEFT = df.LEFT
	MARGIN = df.MARGIN
	#SETUP THE WINDOW
	WINDOWWIDTH = df.WINDOWWIDTH
	WINDOWHEIGHT = df.WINDOWHEIGHT
	#SET UP COLORS
	BLACK = df.BLACK
	RED = df.RED
	GREEN = df.GREEN
	WHITE = df.WHITE
	MSG_POS = (0, WINDOWHEIGHT)
	#INITIALIZE SCREEN
	screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
	pygame.display.set_caption('RLTankAttack - Reinforcement Learning Game')
	#WHILE LOOP VARIABLES
	runApp = True
	i = 1
	line1 = False
	showWaters = True
	#CREATE BOATS LIST OF SPRITES
	boats = list()
	#boats.append(Boat([LEFT - STEP, TOP - STEP], "boat_p1", "right", (0, NUMBER_OF_WATERS - 1),BOATS_ARRAY[0]))
	boats.append(
				Boat("boat_0",BOATS_ARRAY[0],screen)
				)	
	boats.append(
				Boat("boat_1",BOATS_ARRAY[1],screen)
				)	
	print boats[0].get_boat_id()
	print boats[1].get_boat_id()

	
	x,y = boats[1].get_coords()
	print x,y
	exit()
	message = Message(MSG_POS, "RLTankAttack - gezerlis@gmail.com")

	#VALVES CREATION
	valves = list()
	vcol = 0
	for j in range (LEFT, LEFT + (NUMBER_OF_WATERS) * STEP + NUMBER_OF_WATERS * MARGIN, STEP + MARGIN):
		valves.append(Valve([j + IMAGE_HEIGHT / 2, BOTTOM + IMAGE_HEIGHT], True, vcol));
		valves.append(Valve([j + STEP / 2 + IMAGE_HEIGHT / 2, BOTTOM + IMAGE_HEIGHT], False, vcol));
		vcol += 1
	
	#CREATE SURROUNDING EARTH LIST OF SPRITES
	earth = list()
	for j in range (BOTTOM + STEPy, TOP, -STEPy):
		earth.append(Earth([LEFT - STEP, j]))
	for j in range (BOTTOM + STEPy, TOP, -STEPy):
		earth.append(Earth([LEFT + (NUMBER_OF_WATERS - 1) * STEP + NUMBER_OF_WATERS * MARGIN + STEP, j]))
	for j in range (LEFT - STEP, LEFT + (NUMBER_OF_WATERS) * STEP + NUMBER_OF_WATERS * MARGIN, STEP + MARGIN):
		earth.append(Earth([j, BOTTOM + STEPy]))
	
	#WHICH BOAT IS ABOUT TO PLAY - 0 left, 1 right
	BOATS_TURN = 0
	
	#MAIN WHILE LOOP
	while runApp:
		#FILL SCREEN WITH BLACK COLOR BACKGROUND
		screen.fill(BLACK)
		#ADD BOATS LIST TO SCREEN
		for b in boats:
			b.draw()
		#ADD EARTH LIST TO SCREEN
		for e in earth:
			e.draw(screen)
		#ADD CANALS LIST OF SPRITES
		waters = list()
		waters_buffered = list()
		k = HEIGHT_OF_WATER - 1
		#ITERATE AGAINST WATER_LEVEL MATRIX
		m = 0
		mtrx_cid = list()
		mtrx_bid = list()
		for i in range(0, NUMBER_OF_WATERS):
			for j in range (BOTTOM, TOP, -STEPy):
				if WATER_LEVEL[k][i] == True:
					waters.append(Water([LEFT + i * STEP + i * MARGIN, j]))
					mtrx_cid.append(((i, k), m))
					m += 1
				else:
					waters.append(Water([LEFT + i * STEP + i * MARGIN, j + TOP + HEIGHT_OF_WATER * STEP + STEP / 2]))
					mtrx_cid.append(((i, k), m))
					mtrx_bid.append(((i, k), m))
					m += 1
				k -= 1
			k = HEIGHT_OF_WATER - 1
		#ADD WATER CANALS LIST TO SCREEN
		if(showWaters):
			for w in waters:
				w.draw(screen)
		
		#ADD VALVES LIST TO SCREEN
		for v in valves:
			v.draw(screen)
		
		#ADD MESSAGE TEXT
		message.draw(screen)
	
		#SHOW WHOS TURN IT IS ARROW
		if(BOATS_TURN == 0):
			WHOS_TURN = WhosTurn((WINDOWWIDTH / 3, WINDOWHEIGHT / 2 + 3 * STEPy), True)
		elif(BOATS_TURN == 1):
			WHOS_TURN = WhosTurn((WINDOWWIDTH * 2 / 3, WINDOWHEIGHT / 2 + 3 * STEPy), False)
		WHOS_TURN.draw(screen)
		#update screen and fill with black
		pygame.display.update()

		##################MOUSE ACTIONS#####################
		##################MOUSE  OBJECT#####################
		mymouse = pygame.event.wait()
		if(mymouse.type == pygame.QUIT):
			exit()
		if(mymouse.type == MOUSEBUTTONDOWN):
			#MOUSE CLICKED OVER VALVE
			for v in valves:
				if v.over(mymouse.pos):
					vstr = "Boat: " + str(BOATS_TURN) + " Column:" + str(v.get_column_of_water()) + " Up:" + str(v.lookingUp())
					message = Message(MSG_POS, vstr)
					BOATS_TURN = WHOS_TURN.changeTurn(BOATS_TURN)
					if v.lookingUp() == False:
						WATER_LEVEL = f.pop_water(WATER_LEVEL, v.get_column_of_water())
					else:
						WATER_LEVEL = f.push_water(WATER_LEVEL, v.get_column_of_water())
					break
			#MOUSE CLICKED OVER BOAT
			for b in boats:
				if(b.over_point(mymouse.pos)):
					print "clicking over boat", b.get_boat_id()
					break
		mainClock.tick(60)	

def msg(txt):
	message = Message((100, 200), txt)
	
if __name__ == '__main__':
	main()

