from random import choice
import numpy as np

map_dim_NS = 10 #north south dimension of game map
map_dim_EW = 10 #east west
map_dim_UD = 3 #uyp down
levels = [str(i) for i in range(map_dim_UD)]
ground_level = 1

user_input = ""
current_coords = [0,0,0]
inventory = []

curses = ["fuck","shit","damn","crap","cunt","twat","dick","ass","asshole"]
curse_responses = ["Grow up","Don't be a twat","You kiss your mother with that mouth?","So... nothing usefull to say?","Seriously?"]

look_synonyms = ["look","gaze","view","examine"]

directions = ["north","south","east","west","up","down","around"]



action = ""
subject1 = ""
subject2 = ""




class location():
	def __init__(self,loc):
		self.loc
	"""
	def look(self,direction):
		if direction == "north" and :
			"""

class object_obtainable():
	def __init__(self):
		pass

class object_fixed():
	def __init__(self):
		pass

class entity():
	def __init__(self):
		pass



class the_void(location):
	def __init__(self):
		self.name = "The Void"
		self.discovered = False


class ship(location):
	def __init__(self):
		self.name = "ship"
		self.discovered = True

def show_map(Map,lvl):
	viewable_map_level = [[game_map[lvl][j][i].name if game_map[lvl][j][i].discovered else " " for i in range(map_dim_EW)] for j in range(map_dim_NS)]
	"""
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in viewable_map_level]))
	"""
	print(np.matrix(viewable_map_level))


def input_parser(ui):
	word_list = ui.lower().split(" ")
	global action
	global subject1
	global subject2
	action = ""
	subject1 = ""
	subject2 = ""
	for word in word_list:
		if word in curses:
			print(choice(curse_responses))
			break
		if word in look_synonyms:
			action = "look"
		if word in directions:
			subject1 = word
		if word == "map":
			subject1 = word
		if subject1 == "map" and word in levels:
			subject2 = word
			
			
			
			


def input_handle():
	if action == "":
		pass
	elif action == "look":
		if subject1 == "around":
			print("you look around") #this will be replaced, just testing now
		elif subject1 == "map":
			if subject2 not in levels:
				print("You must specify which level of the map you would like to look at. Ground level is {}".format(ground_level))
			else:
				show_map(game_map,int(subject2))
	



void_loc = the_void()
ship_start = ship()


game_map = [[[void_loc for i in range(map_dim_EW)] for j in range(map_dim_NS)] for k in range(map_dim_UD)]  #coords are z,y,x

game_map[1][5][5] = ship_start

#***************** Setup *****************











#********************* Main Loop *******************
while user_input != "exit":
	user_input = input("What do you do? ")
	input_parser(user_input)
	input_handle()
	
	if user_input == "map":
		for i in range(map_dim_EW):
			print(game_map[0][i])
				
	
	
