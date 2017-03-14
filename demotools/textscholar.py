#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" textual scholar functions for importing and cleaning data """
__author__      = "mr. thump"

import io, os, re
from lxml import html    
from unidecode import unidecode
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import numpy as np
from collections import defaultdict
from nltk.corpus import stopwords
# TODO
def vanilla_folder(filepath):
    files = os.listdir(filepath)
    os.chdir(filepath)
    docs = []
    titles = []
    for file in files:
        with io.open(file,'r',encoding = 'utf8') as f:
            vanilla = f.read()
            docs.append(vanilla)
            titles.append(re.sub(r'\.txt$', '', file))
            f.closed
    return docs, titles
# TODO
def xml_folder(filepath):
    files = os.listdir(filepath)
    os.chdir(filepath)
    docs = []
    titles = []
    for file in files:
        print "file import: " + file
        h = html.parse(open(file))
        tei = h.xpath('//l') # lines
        titles.append(h.xpath('//title')[0].text)
        n = len(tei)
        lignes = [None]*n
        for i in range(n):
            lignes[i] =  tei[i].text
        lignes = filter(None, lignes)    
        docs.append(lignes)
    docs_str =[]
    for doc in docs:
        docs_str.append(" ".join(doc))
    return docs, titles, docs_str
# TODO
def norm_unicode(docs):
    normdocs = []
    regex = re.compile("['()\*\-,\.\:!?<>0-9]")
    for doc in docs:
        doc = doc.lower()
        #doc = unidecode(doc)
        doc = regex.sub('',doc)
        normdocs.append(doc)
    return normdocs
# TODO
def tokenize_list(docs):
    unigrams = [[w for w in doc.split()] for doc in docs]
    return unigrams
# TODO
def stopfilter_list(docstoken, lang = "english"):
    sw = stopwords.words(lang)   
    # sw = io.open("/home/kln/Documents/education/text_scholar/resources/stopwords_da.txt",'r',encoding = 'utf8').read().lower().split() 
    output = []
    for tokens in docstoken:
        output.append([token for token in tokens if token not in sw])
    return output    
# TODO
def stem_list(docstoken,lang = "danish"):
    stemmer = SnowballStemmer(lang, ignore_stopwords = True)
    docsstem = [[stemmer.stem(w) for w in token] for token in docstoken]
    return docsstem
# TODO
def prune(unigrams,mxper,mnper):
    frequency = defaultdict(int)
    for doc in unigrams:
        for unigram in doc:
            frequency[unigram] += 1
    freqs = [val for val in frequency.values()]
    mn = np.percentile(freqs, mnper)
    mx = np.percentile(freqs, mxper)
    unigrams_prune = [[unigram for unigram in doc if frequency[unigram] > mn and frequency[unigram] <= mx] for doc in unigrams]
    return unigrams_prune
# TODO
def prune_n(docs, mxn, mnn = 1):
    frequency = defaultdict(int)
    for doc in docs:
        for token in doc:
            frequency[token] += 1
    freqs = sorted([val for val in frequency.values()], reverse = True)
    mx = freqs[mxn - 1]
    mn = freqs[- mnn]
    output = [[token for token in doc if frequency[token] >= mn and frequency[token] <= mx] for doc in docs]
    return output
# TODO
def get_metadata(metadata, titles, docnum):
    titles_df = pd.DataFrame(np.zeros(shape = (len(titles), 2)))    
    for i in range(len(titles)):
        titles_df.iloc[i,:] = map(int,titles[i].split('_'))
    target_df = metadata.loc[metadata.iloc[:,0] == titles_df.iloc[docnum,0],:]    
    return (target_df.loc[target_df.iloc[:,1] == titles_df.iloc[docnum,1],:]).reset_index()




