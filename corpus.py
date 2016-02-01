import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications", "A survey of user opinion of computer system response time", "The EPS user interface management system", "System and human system engineering testing of EPS", "Relation of user perceived response time to error measurement", "The generation of random binary unordered trees", "The intersection graph of paths in trees", "Graph minors IV Widths of trees and well quasi ordering", "Graph minors A survey"]

#remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

#remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
	for token in text:
		frequency[token] += 1 

texts = [[token for token in text if frequency[token] > 1] for text in texts]

from pprint import pprint #print 
pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('C:/Users/Kimia/Documents/GitHub/Latent-Semantic-Analysis/tmp/deerwester.dict') #store dictionary for future reference
print(dictionary)

#convert a tokenized doc to a vector
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split()) #doc2bow counts number of occurrences of each word and converts to integer word id and returns as sparse vector; interaction doesnt show up since not in original document
print(new_vec)

#convert from dictionary to corpus, or sparse vector that shows number of times of word
corpus = [dictionary.doc2bow(text) for text in texts]
#MmCorpus is storing corpus in market matrix format, which is a sparse matrix
corpora.MmCorpus.serialize('C:/Users/Kimia/Documents/GitHub/Latent-Semantic-Analysis/tmp/deerwester.mm', corpus) #save to disk for later use
print(corpus)
#saving to disk is better than to RAM, if corpus ends up being millions of docs long


