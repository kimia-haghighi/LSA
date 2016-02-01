import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#we previously created a corpus, now we will use gensim and use this corpus
#will transform documents from one vector to another in order to:
	#1. bring out hidden structure in the corpus, and discover neew relations between words and sue them to describe doc in new way
	#2. make the doc representation more compact. this improves efficency and efficacy (marginal data trends are ignored, noise reduction)
from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('C:/Users/Kimia/Documents/GitHub/LSA/tmp/deerwester.dict'

#transformations are standard python objects initialized by a training corpus
tfidf = models.TfidfModel(corpus) #step 1 -- initialize a model
