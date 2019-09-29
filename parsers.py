import os

def parse(file, id):
	'''
		Converts file contents into plain text using texttract and stores it in corpus/op/ with the given id.
		Returns True if file is sucessfully converted.
		Returns False if conversion fails or file is empty.
		(Note: .doc and.pkl files are ignored and will return False)
	'''
	# check if file is not .doc or .pkl
	if(file.split(".")[-1] in ["doc", "pkl"]):
		return False
	import textract as tx 
	try:
		txt = tx.process(file).decode('utf-8')	# convert file contents to string using texttract
		if (txt != ""):
			with open("corpus/op/"+str(id)+".txt", "w", encoding="utf-8") as op:
				op.write(txt)	# write to text file
				return True
		else:
			# if file is empty
			with open("err.txt", "a", encoding="utf-8") as op:
				op.write("Empty: " + file + "\n")		
			return False
	except:
		with open("err.txt", "a", encoding="utf-8") as op:
			op.write("Failed: " + file + "\n")
		return False

def explore(dir = os.getcwd()):
	'''
		Returns a list of all supported files 
		(Note: .doc and .pkl files are not supported by textract)
	'''
	# supported formats
	formats = ["csv", "doc", "docx", "eml", "epub", "gif", "htm", "html", "jpeg", "jpg", "json", "log", "mp3", "msg", "odt", "ogg", "pdf", "pkl", "png", "pptx", "ps", "psv", "rtf", "tff", "tif", "tiff", "tsv", "txt", "wav", "xls", "xlsx"]
	files = []

	# explore directory and subdirectories recursively
	for f in os.listdir(dir):
		if(os.path.isdir(os.path.join(dir, f)) and dir not in ["op", "corpus", "templates"] and dir[0] not in ["!", "_", "."]):
			files = files + explore(os.path.join(dir, f))
		elif(os.path.isfile(os.path.join(dir, f)) and f.split('.')[-1] in formats):
			# store paths to supported files
			files.append(os.path.join(dir, f))
	return files

def doc2x(dir = os.getcwd()):
	'''
		Converts all .doc files in directory and subdirectory to .docx and stores them in doc2/ 
	'''
	import subprocess
	files = explore(dir)
	for f in files:
		if(f.endswith(".doc")):
			subprocess.call(['soffice', '--headless', '--convert-to', 'docx', '--outdir', dir + '/doc2', f])

if __name__ == '__main__':
 	print(explore(os.getcwd()))
