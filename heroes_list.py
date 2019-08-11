import pathlib
from random import randint

# Heroes path
the_path = pathlib.Path.cwd() / 'Heroes'

# Specific heroes path
dc_heroes_path = the_path / 'dc_comic' # Folder where DC Comics heroes are
marvel_heroes_path = the_path / 'marvel' # Folder where Marvel heroes are
hyper_heroes_path = the_path / 'hyper' # Folder where hyper heroes are

dc_heroes_list = []
marvel_heroes_list = []
hyper_heroes_list = []

# Let's define a function which take a path and list in which fill out
# heroes name

def fill_out_heroes_name(path, the_list):
	""" Take a path.
	In this path, get all files which can be found.
	Next, for each file, get only the name without extension, and fill out
	the list which passed in arguments with these names.
	"""

	# 1rst method
	for the in path.rglob('*'):
		the_name = the.stem # get the name of file without it's extension
		the_list.append(the_name) # fill out the list


	'''Another method: using os module (2nd method)
	As we know that all files have same extension (.pdf), we could procceded
	by use listdir method (os module) firstly and then, remove the extension
	by removing 4 last character of each file name.

	the_files = os.listdir(path) # get all files which can be found
	for names in the_files:
		the_name = names[:-4] # get the name of file without it's extension
		the_list.append(the_name)
	'''

	return the_list

def fill_on_number(team_number):
	"""Get team number and fill out correct list """

	#NOTE: team number based on main scenario in heroes.py

	if team_number == 1:
		heroes_team = fill_out_heroes_name(dc_heroes_path, dc_heroes_list)
	elif team_number == 2:
		heroes_team = fill_out_heroes_name(hyper_heroes_path, hyper_heroes_list)
	else:
		heroes_team = fill_out_heroes_name(marvel_heroes_path, marvel_heroes_list)

	return heroes_team

# At end, i want to create a function which choose randomly two or three 
# heroes pictures 

def choose_bonus_picture(heroes_list):
	""" Get a list a return two or three heroe in this list """

	# choose if we want get two or three heroes pictures as bonus
	bonus_heroes_number = randint(2, 3)

	heroes = []

	for x in range(0, bonus_heroes_number):
		heroes_list_length = len(heroes_list)

		the_heroe_name = heroes_list[randint(0, heroes_list_length-1)]

		while the_heroe_name in heroes:
		 	the_heroe_name = heroes_list[randint(0, heroes_list_length-1)]
		
		heroes.append(the_heroe_name)

	return heroes

def choose_cover_page(heroes_list):
	"""Choose in a list one heroe for cover page"""

	choosen_num = randint(0, len(heroes_list)-1)

	return heroes_list[choosen_num]