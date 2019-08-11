import pathlib
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
import heroes_list


def conceive_book(player_name, heroe_team, cover_heroe, player_score,
				  quiz_summary, bonus_pictures):
	
	"""Use arguments to create a pdf book"""

	the_heroes_path = pathlib.Path.cwd() / f'{heroe_team}'
	bonus_pictures_names = [] # use list to collect bonus pictures

	# define generated book name (with its extension)
	output_file_name = pathlib.Path.cwd() / 'Edited_books' / f'quiz result of {player_name}.pdf'
	output_file = open(output_file_name, 'wb')

	output_pdf = PdfFileWriter()

	# Introduction text with player name
	intro_text = f'Mega heroes quizz with {player_name}'

	# The cover page
	cover_page_name = the_heroes_path / f'{cover_heroe}'
	cover_page = PdfFileReader(open(cover_page_name, 'rb'))

	# store player score into a variable
	display_score = f'Score: {player_score}/20 | {player_score*100 / 20}%'

	# Create book
	output_pdf.addPage(cover_page.getPage(0)) # add cover page

	''' For add some pages, i'll need to create them and then, 
	add them to final pdf file. These files will be at "trash_pdf" folder.
	'''

	# let's create a pdf page which will store intro text and player score
	trash_path = pathlib.Path.cwd() / 'trash_pdf'
	intro_path = trash_path / 'intro.pdf'
	intro_pdf = canvas.Canvas(f'{intro_path}')
	intro_pdf.setFont('Helvetica', 28)
	intro_pdf.drawString(50, 500, f'{intro_text}')
	intro_pdf.setFont('Helvetica', 18)
	intro_pdf.drawString(200, 450, f'{display_score}')
	intro_pdf.save()

	intro_file = PdfFileReader(open(intro_path, 'rb'))
	output_pdf.addPage(intro_file.getPage(0))

	# add quiz summary
	quiz_summary_path = trash_path / 'quiz_summary.pdf'
	quiz_summary_pdf = canvas.Canvas(f'{quiz_summary_path}')
	quiz_summary_pdf.setFont('Helvetica', 28) # set title font
	quiz_summary_pdf.drawString(180, 700, 'Quiz summary') # write title
	quiz_summary_pdf.setFont('Helvetica', 11) # set font for other lines
	line_height_level = 600
	i = 1
	for key_value, info_value in quiz_summary.items():
		quiz_summary_pdf.drawString(10, line_height_level, f'{key_value} {info_value}')

		if i % 2 == 0:
			line_height_level -= 50
		else:
			line_height_level -= 20

		i += 1
	quiz_summary_pdf.save()

	quiz_summary_file = PdfFileReader(open(quiz_summary_path, 'rb'))
	output_pdf.addPage(quiz_summary_file.getPage(0))

	# add bonus pictures
	for picture in bonus_pictures:
		picture_file_name = the_heroes_path / f'{picture}.pdf'
		picture_file = PdfFileReader(open(picture_file_name, 'rb'))
		output_pdf.addPage(picture_file.getPage(0))

	output_pdf.write(output_file) # write all output_pdf content in output_file
	output_file.close()
