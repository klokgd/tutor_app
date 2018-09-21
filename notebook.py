
noteName = 'notebook.txt'

class Note:
	"""docstring for Note"""
	def __init__(self, newNote, newAuthor):
		self.newNote = newNote
		self.newAuthor = newAuthor
		print("Ваша запись: {0}".format(self.newNote))
	def addNote(self):
		f = open(noteName, 'a')
		f.write("{0} {1} \n".format(self.newNote, self.newAuthor))
		f.close()
		print("Запись успешно добавлена!")


running = True

while running:
	print("Хотите добавить запись в книгу? y/n")
	n = input()
	if n == "y": 
		newNote = Note(input('Введите номер: '), input('Введите имя: '))
		newNote.addNote()		
	elif n == "n":
		running = False
	else:
		print('Error')

while  running:
	pass
