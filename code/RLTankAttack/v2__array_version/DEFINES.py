import numpy as np 
WATER_LEVEL = np.array([
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1]
	], dtype=bool)

HEIGHT_OF_WATER = len(WATER_LEVEL)
NUMBER_OF_WATERS = len(WATER_LEVEL[0])

#PARAMS
IMAGE_WIDTH_HEIGHT = 40
IMAGE_HEIGHT = 10
TOP = 60
BOTTOM = HEIGHT_OF_WATER * IMAGE_HEIGHT + TOP
STEP = IMAGE_WIDTH_HEIGHT
STEPy = IMAGE_HEIGHT
LEFT = 80
MARGIN = 0
#SETUP THE WINDOW
WINDOWWIDTH = 2 * LEFT + (NUMBER_OF_WATERS) * STEP + (NUMBER_OF_WATERS + 1) * MARGIN
WINDOWHEIGHT = 2 * (BOTTOM) + 3 * TOP + 2 * STEPy

#SET UP COLORS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
