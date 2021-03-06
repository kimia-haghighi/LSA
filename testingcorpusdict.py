import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications", "A survey of user opinion of computer system response time", "The EPS user interface management system", "System and human system engineering testing of EPS", "Relation of user perceived response time to error measurement", "The generation of random binary unordered trees", "The intersection graph of paths in trees", "Graph minors IV Widths of trees and well quasi ordering", "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
	for token in text:
		frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]

from pprint import pprint   # pretty-printer
pprint(texts)


#create a dictionary file, so we don't have to run from memory, which gets annoying when indexing millions of docs
dictionary = corpora.Dictionary(texts)
dictionary.save('C:/Users/Kimia/Documents/GitHub/LSA/tmp/deerwester.dict') # store the dictionary, for future reference
print(dictionary)


#create a corpus, which creates a sparse matrix, in matrix market format (MmCorpus). using doc2bow converts from tokens to number of instances.
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('C:/Users/Kimia/Documents/GitHub/LSA/tmp/deerwester.mm', corpus) # store to disk, for later use
print(corpus)

