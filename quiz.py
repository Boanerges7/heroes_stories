import pathlib
import csv
import random


# Common path
questions_path = pathlib.Path.cwd() / 'Questions'

# Specific questions source path
dc_questions_src_path = questions_path / 'dc_questions.txt'
hyper_questions_src_path = questions_path / 'hyper_questions.txt'
marvel_questions_src_path = questions_path / 'marvel_questions.txt'

# Specific questions destination path
dc_questions_dest_path = questions_path / 'dc_questions.csv'
hyper_questions_dest_path = questions_path / 'hyper_questions.csv'
marvel_questions_dest_path = questions_path / 'marvel_questions.csv'

questions_list = [] # we'll store questions in here
quiz_resume = {} # store player game
question_num = 1 # asked question number
score = 0 # player score

def write_heroes_questions(txt_path, csv_path):
	"""Take a txt file and write a csv file from it
	with two main informations:
	- the question
	- the answer"""

	questions_dict = {} # it will collect questions and answers

	# Fill out questions dictionary with questions and answers
	with open(txt_path, 'r') as source_file:
		for question_answer in source_file:
			the_question = question_answer.split(':')[0] # get the question
			the_answer = question_answer.split(':')[1] # get the answer
			the_answer = the_answer.rstrip()
			questions_dict[the_question] = the_answer

	'''Note:
	1) We use split method to convert into list questions and answers,
	also seperate questions to answers and assign them to correct
	variables. As we know, first part (or left part) corresponds to 
	question and second part (or right part) corresponds to answer.
	2) We use rsplit method for removing newlines in answers.
	'''

	# Write csv file from questions dictionary
	with open(csv_path, 'w') as the_file:
		csv_writer = csv.writer(the_file)
		csv_writer.writerow(['Question', 'Answer']) # write header of csv file

		for question, answer in questions_dict.items():
			csv_writer.writerow([question, answer])


'''Now we can learn and write a csv file from txt file, define a function
which read a csv file and ask questions
'''

def assign_heroes_questions(csv_file):
	"""Get a csv file, then write questions and answers"""

	questions_answers_dict = {}

	with open(csv_file, 'r') as the_file:
		questions_answer = csv.reader(the_file)

		next(questions_answer)

		for line in questions_answer:
			the_question = line[0]
			the_answer = line[1]
			questions_answers_dict[the_question] = the_answer
			questions_list.append(the_question)

	return questions_answers_dict

def ask_heroes_questions(csv_file, quiz_resume):
	"""Ask questions randomly"""

	questions_answer = assign_heroes_questions(csv_file)
	choosen_question = random.choice(questions_list)

	user_answer = input(f'{choosen_question}: ')
	correct_answer = ''
	global score
	global question_num

	for question_value, answer_value in questions_answer.items():
		if choosen_question == question_value:
			if user_answer.lower() == answer_value:
				print(f'Great: your answer is correct: {answer_value}')
				score += 4 # gain scores
			else:
				print(f'No! You\'ve failed. The correct answer is: {answer_value}')

			print(f'Your score: {score}pt')

			quiz_resume[f'Question n°{question_num}: {choosen_question}'] = f'Correct answer: {answer_value}'
			quiz_resume[f'Your answer at question n°{question_num}: '] = f'{user_answer}'
			question_num += 1
