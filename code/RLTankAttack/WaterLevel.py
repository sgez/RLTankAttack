import DEFINES as df

class WaterLevel():
	def __init__(self):
		self.WATER_LEVEL = df.WATER_LEVEL

	def pop_column(self,col):
		for i in range(df.HEIGHT_OF_WATER):
			if(df.WATER_LEVEL[i][col]==True):
				df.WATER_LEVEL[i][col] = False
				break
		return df.WATER_LEVEL
	
	def push_column(self,col):
		for i in range(df.HEIGHT_OF_WATER-1,-1,-1):
			if(df.WATER_LEVEL[i][col]==False):
				df.WATER_LEVEL[i][col] = True
				break
		return df.WATER_LEVEL
		
	
	def water_level(self):
		return df.WATER_LEVEL
	
	def get_column_height(self,col):
		for i in range(df.HEIGHT_OF_WATER-1,-1,-1):
			print i
			if(df.WATER_LEVEL[i][col]==False):
				break
		return i