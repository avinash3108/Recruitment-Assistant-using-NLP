import nltk
import pickle as pkl
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import numpy as np
import parsers as pr
from scipy import spatial
import pandas as pd
import os 
def run(jd,corpus):
	model = Word2Vec.load('w2v_model')
	w2v = []
	jd = [PorterStemmer().stem(word) for word in nltk.word_tokenize(jd) if word not in stopwords.words('english') and word.isalnum()]
	for word in jd:
		if word in model.wv.vocab:
			w2v.append(model.wv[word])
	vjd = np.mean(w2v, axis=0)

	vcv = []
	for cvs in corpus:
		w2v = []
		with open(cvs, 'rb') as f:
			cv = pkl.load(f)
			for word in cv:
				if word in model.wv.vocab:
					w2v.append(model.wv[word])
		vcv.append((np.mean(w2v, axis=0), cvs.split('/')[-1].split('.')[0]))

	res = []
	for i in range(0, len(vcv)):
		res.append((1 - spatial.distance.cosine(vjd, vcv[i][0]), vcv[i][1]))
	#for i in range(0, len(cvc)):
	#   retrieval.append((1 - spatial.distance.cosine(vjd, vcv[i][0]), vcv[i][1]))

	res.sort(reverse=True)
	print(res[:15])
	
	with open('oput.pkl', 'wb') as op:
		pkl.dump(res, op)

	df = pd.read_csv("db.csv")
	response = {'cid':[], 'score':[], 'path':[]}
	for i in range(20):
		response['cid'].append(res[i][1])
		response['score'].append("{:.1f}".format(res[i][0]*100))
		response['path'].append(df[df['cid']==int(res[i][1])]['cv'].values[0])

	return response

if __name__ == '__main__':
	with open('jd.txt', 'r') as jd:
		gg = jd.read()

	result = run(gg, pr.explore('corpus/tokenized'))
	print(pd.DataFrame(result))




