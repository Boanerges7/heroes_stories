import heroes_list
import book
import quiz
import pathlib
from PyPDF2 import PdfFileReader, PdfFileWriter


print('Welcome to MEGA HEROE QUIZ!')
player_name = input('Please, enter your name (max: 13 characters): ')
game_over = False
correct_choice = False
player_team = []
team_folder = ''

while not player_name or player_name == ' ' or len(player_name) > 13:
	player_name = input('Please, enter your name (max: 13 characters): ')

print(f'Well {player_name}! now, next step.')

while not correct_choice:

	player_team_num = input(f'Choose your team number:\n\
1- DC Comic team\n\
2- Hyper team\n\
3- Marvel team\n\
')

	# Check that player choice is a number and is between 1 and 3
	try:
		player_team_num = int(player_team_num)
		correct_choice = True

		if player_team_num < 1 or player_team_num > 3:
			correct_choice = False
			print('Make sure to choose a team number.')
		else:
			correct_choice = True
	except ValueError:
		print('Sorry, you didn\'t choose a team number.')
		correct_choice = False

	# Fill out correct team list
	player_team = heroes_list.fill_on_number(player_team_num)

# Now, show him chosen team members.
print(f'\nGreat! Check your team hereoes.')
for heroe in player_team:
	print(f'- {heroe}')

def quiz_process(player_team_num):
	"""Belongs to player team num, proceed to questions"""

	if player_team_num == 1:
		questions_src = quiz.dc_questions_src_path
		questions_dest = quiz.dc_questions_dest_path
		team_folder = 'dc_comic'

	elif player_team_num == 2:
		questions_src = quiz.hyper_questions_src_path
		questions_dest = quiz.hyper_questions_dest_path
		team_folder = 'hyper'
	else:
		questions_src = quiz.marvel_questions_src_path
		questions_dest = quiz.marvel_questions_dest_path
		team_folder = 'marvel'

	# Write questions
	quiz.write_heroes_questions(questions_src, questions_dest)

	# Ask questions
	quiz.ask_heroes_questions(questions_dest, quiz.quiz_resume)

	return team_folder

print('Now, it\'s quiz time!\n')

for i in range(0, 5):
	the_team = quiz_process(player_team_num)

# Book conception
heroes_name_list = heroes_list.choose_bonus_picture(player_team)
cover_page = heroes_list.choose_cover_page(heroes_name_list)
heroes_team = pathlib.Path.cwd() / 'Heroes' / f'{the_team}'
cover_heroe = heroes_team / f'{cover_page}.pdf'

book.conceive_book(player_name, heroes_team, cover_heroe,
				   quiz.score, quiz.quiz_resume, heroes_name_list)
