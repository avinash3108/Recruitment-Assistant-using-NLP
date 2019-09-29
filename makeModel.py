import nltk
import pickle
import parsers as pr 
from gensim.models import Word2Vec

def train_model(model_name, corpus_dir = 'corpus/tokenized/'):
	files = pr.explore(corpus_dir)
	tkns = [] 
	for file in files:
		with open(file, 'rb') as f:
			tkns.append(pickle.load(f))

	model = Word2Vec(tkns, size=300, window=5, sg=1)
	model.save(model_name)
	return True

if __name__ == '__main__':
	if(train_model('w2v_model', 'corpus/tokenized/')):	print("Model trained")



