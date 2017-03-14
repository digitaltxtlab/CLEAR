#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: flat topic model using latent Dirichlet allocation """
__author__      = "K.L. Nielbo"

import os
os.chdir("/home/kln/Documents/education/text_scholar/code.py")
import textscholar as ts
import numpy as np
from pandas import read_table

## import texts
#somedir = "/home/kln/Documents/education/text_scholar/data/txt/"
#adl_metadata = read_table("/home/kln/Documents/education/text_scholar/data/adl_index.txt", header = None, encoding = 'utf-8')

somedir = "/home/kln/Documents/projects/clear_local/CLEAR/31_11995_G"
texts, titles = ts.vanilla_folder(somedir)
texts = ts.norm_unicode(texts)
texts = ts.tokenize_list(texts)
texts = ts.stopfilter_list(texts, lang = "danish")
texts = ts.prune_n(texts,100)

#texts = ts.stem_list(texts)

#from gensim.utils import chunkize
#def chunk_token(unigrams,n):
#    chunks = []
#    for doc in unigrams:
#        clen = len(doc)/n
#        for chunk in chunkize(doc,clen):
#            chunks.append(chunk)
#    return chunks
# docschunks = chunk_token(docstoken,5)

## train LDA model
from gensim import corpora, models
## bag-of-words model
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(chunk) for chunk in texts]

# inspect bag of words representation of document
i = 200
print ts.get_metadata(adl_metadata, titles, i)
print titles[i]
print texts[i]
len(texts[i])
adoc = corpus[i]
for ii in range(len(adoc)):
    print dictionary[adoc[ii][0]] + ', ' + str(adoc[ii][0]) + ':' + str(adoc[ii][1])

##  train model on k topics
np.random.seed(23) # for reproducibility
k = 20
mdl = models.LdaModel(corpus, id2word=dictionary, num_topics=k)#, chunksize=3125, passes=25, update_every=0, alpha=None, eta=None, decay=0.5, distributed=False)
# export model
# mdl.save('/home/kln/Documents/education/text_scholar/data/mdl.lda')
import gensim
mdl = gensim.models.LdaModel.load('/home/kln/Documents/education/text_scholar/data/mdl.lda')

# inspect topics
for i in range(20):
    print 'Topic', i
    print(mdl.show_topic(i,10))
    print('-----')
# get topic distribution for a documents
mdl.get_document_topics(adoc, minimum_probability=0)
# or simply the most likely topics
print mdl[adoc]

# query model on particular set of words
query = 'Jesus og Odin er venner'
query = u'Ifølge Peter Madsen er Jesus og Odin venner'
query = query.lower().split()
vocab = dictionary.values()
query = [w for w in query if w in vocab]
query = dictionary.doc2bow(query)
mdl[query]
print mdl.show_topic(17,10)
