import subprocess
import os
import parsers as pr
from initData import create_txts
from preprocessCorpus import prepare_corpus
from makeModel import train_model

# ensure desired directory structure
if not (os.path.exists('resumes')):
	os.makedirs('resumes/doc2/')
if 'doc2' not in os.listdir('resumes'):
	os.makedirs('resumes/doc2/')
if not (os.path.exists('corpus')):
	os.makedirs('corpus/op/')
	os.makedirs('corpus/tokenized/')
if 'op' not in os.listdir('corpus'):
	os.makedirs('corpus/op/')
if 'tokenized' not in os.listdir('corpus'):
	os.makedirs('corpus/tokenized/')

print("[Directory Structure OK]")

# check if CVs are available in resumes folder
if pr.explore('resumes/')==[]:
	print("No CVs available, please put CVs in 'resumes' folder.")
	exit()

# (re)create corpus
files = pr.explore('corpus/op/')
if files!=[]:
	ch = input('Recreate corpus? (y/n)')
	if ch.lower() in ['y', 'yes']:
		for tmp in pr.explore('resumes/doc2'):
			os.remove(tmp)
		for tmp in files:
			os.remove(tmp)
		create_txts('resumes')
		print('[Conversion to plain text done]')
		prepare_corpus('corpus/')
		print('[Tokenized corpus created]')
	else:
		print('Using old plain text corpus. If there is any change in the resume pool, this will lead to errors.\n'+
			  'Incase of errors, recreate the plain text corpus.')
else:
	create_txts('resumes')
	print('[Conversion to plain text done]')
	for tmp in files:
		os.remove(tmp)
	prepare_corpus('corpus/')
	print('[Tokenized corpus created]')

try:	
	if train_model('w2v_model', 'corpus/tokenized/'):	print('[Model trained]')
except:
	print('Error occured while training the model')
	import traceback
	traceback.print_exc()
	exit()

print("\n[Build Complete]")