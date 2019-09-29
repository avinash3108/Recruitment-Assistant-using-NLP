import os 
import nltk
import parsers as pr
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pickle as pkl

def prepare_corpus(corpus_dir = 'corpus/'):
	txt_dir = 'op/'
	tkn_dir = 'tokenized/'

	files = pr.explore(corpus_dir + txt_dir)	# list of all plain text CVs in corpus/op/
	print("Files: {}".format(len(files)))

	for file in files:
		with open(file, 'r') as f:
			content = f.read()
			# tokenize, remove stopwords and stem
			content = nltk.word_tokenize(content)
			content = [PorterStemmer().stem(word) for word in content if word not in stopwords.words('english') and word.isalnum()]
			with open(corpus_dir + tkn_dir + file.split('/')[-1].split('.')[0] + '.pkl', 'wb') as pfile:
				pkl.dump(content, pfile)	# dump tokenized text

if __name__ == '__main__':
	prepare_corpus('corpus/')