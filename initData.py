import os
import textract as tx
import parsers as pr
import pandas as pd

### This is used to convert the CVs to plain text and save a mapping of their id and path (db.csv)

def to_txt(dir='resumes/'):
	'''
		convert the CVs to plain text and save a mapping of their id and path		
	'''
	i = 0 	# numeric id
	files = pr.explore(dir)	# get list of all supported files
	
	# lists of cv details
	cv = []
	cv_txt = []
	cv_id = []

	for f in files:
		if(pr.parse(f, i) == 1):
			# add cv details
			cv_id.append(i)
			cv.append(f)
			cv_txt.append('corpus/op/' + str(i) + '.txt')
			i += 1

	d = {'cid':cv_id, 'cv':cv, 'txt':cv_txt}	# make dataframe of cv-id-path mapping
	df = pd.DataFrame(d)
	df.set_index('cid')
	print(df)
	df.to_csv('db.csv')

def create_txts(dir = os.getcwd()):
	pr.doc2x(dir)
	to_txt(dir)

if __name__ == '__main__':
	import parsers as pr
	create_txts('resumes/')
	print("Done. Parsed CVs are store in resumes/op/")
