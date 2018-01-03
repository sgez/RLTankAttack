import pygame, sys, random, time, webbrowser, os, tkMessageBox
import numpy as np
from pygame.locals import *
from Water import Water
from WaterLevel import WaterLevel
from Earth import Earth
from Boat import Boat
from Valve import Valve
from Message import Message
from Functions import Functions
from WhosTurn import WhosTurn
from GameState import GameState
import DEFINES as df
#Win7

def main():
	print sys.version
	# set up pygame
	f = Functions()
	
	pygame.init()
	mainClock = pygame.time.Clock()
	
	#WATER LEVEL MATRIX --- NUMBER_OF_WATERS x HEIGHT_OF_WATER
	#use only df.WATER_LEVEL as a common array
	WATER_LEVEL = df.WATER_LEVEL
	BOATS_ARRAY = np.array([np.invert(df.WATER_LEVEL), np.invert(df.WATER_LEVEL)], dtype=bool)
	BOATS_ARRAY[0][0][0] = 1 #position boat_0 to the left
	BOATS_ARRAY[1][0][len(df.WATER_LEVEL[0]) - 1] = 1 #position boat_1 to the right
	### Code below makes all values of subarray 0 to 0 --> False
	#BOATS_ARRAY[0][:,:][:,:] = 0 #position boat_0 to the left
	### It will be used to clear the array before filling it with boats coords like this:
	# boats[1].draw_boat(BOATS_ARRAY[1])
	### the above attribute sets boats coordinates based on the array
	###
	wl = WaterLevel()

	#print df.HEIGHT_OF_WATER
	'''
	print
	exit()
	'''
	
	
    #BOAT_ROW[0] SHOWS WHERE BOAT 0 IS
	
	HEIGHT_OF_WATER = df.HEIGHT_OF_WATER
	NUMBER_OF_WATERS = df.NUMBER_OF_WATERS
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
				Boat("boat_0", screen)
				)	
	boats.append(
				Boat("boat_1", screen)
				)	

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
	#GAMESTATE object
	game_state = GameState()
	state_winner = False
	#MAIN WHILE LOOP
	while runApp:
		#FILL SCREEN WITH BLACK COLOR BACKGROUND
		screen.fill(BLACK)
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
				if df.WATER_LEVEL[k][i] == True:
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
		
		#ADD BOATS LIST TO SCREEN
		for b in boats:
			b.draw_boat()
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
		event = pygame.event.wait()
		#print event
		vstr = ""
		if(event.type == pygame.QUIT):
			exit()
		if(event.type == MOUSEBUTTONDOWN):
			#MOUSE CLICKED OVER VALVE
			for v in valves:
				if v.over(event.pos):
					if v.lookingUp() == False:
						wl.pop_column(v.get_column_of_water())
						for i in range(2):
							bc = boats[i].get_coords()
							if bc[1]==v.get_column_of_water():
								boats[i].move_down()
						print "============="
						print bc[1]
						print "============="
					else:
						wl.push_column(v.get_column_of_water())
						for i in range(2):
							bc = boats[i].get_coords()
							if bc[1]==v.get_column_of_water():
								boats[i].move_up()
					BOATS_TURN = WHOS_TURN.changeTurn(BOATS_TURN)
					f.log("<pre><MOVE>")
					f.log(wl.water_level())
					f.log(df.BOATS_ARRAY[0])
					f.log(df.BOATS_ARRAY[1])
					f.log("</MOVE></pre>")
					break
			#MOUSE CLICKED OVER BOAT
			for b in boats:
				if(b.over_point(event.pos)):
					print "clicking over boat", b.get_boat_id()
					if(BOATS_TURN == b.get_boat_id()):
						if(event.button==3):
							b.move_right()
						elif(event.button==1):
							b.move_left()
						BOATS_TURN = WHOS_TURN.changeTurn(BOATS_TURN)
						f.log("<pre><MOVE>")
						f.log(wl.water_level())
						f.log(df.BOATS_ARRAY[0])
						f.log(df.BOATS_ARRAY[1])
						f.log("</MOVE></pre>")
						break
			state = game_state.state(df.WATER_LEVEL,df.BOATS_ARRAY)
			print state
			if(state[1] == game_state.BOAT_0_ID):
				vstr = state[0]
				print vstr
				state_winner = True
				f.log("<pre>"+vstr+"</pre>")
			if(state[1] == game_state.BOAT_1_ID):
				vstr = state[0]
				print vstr
				state_winner = True
				f.log("<pre>"+vstr+"</pre>")
		ms = mainClock.tick(60)
		#print "Frame rate: ",ms,"ms"
		if(state_winner):
			url = os.getcwd()+"\\"+f.log_file()
			yes = tkMessageBox.askyesno(message=vstr+"\n\nOpen log file? "+f.log_file()+"",
									icon='question',
									title='GAME OVER')
			if(yes):
				webbrowser.open_new(url)
			exit()
	
if __name__ == '__main__':
	main()

