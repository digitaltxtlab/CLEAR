# Tasks in CLEAR #

First of all, thank you for joining the project, looking forward to working with you. We have dubbed the repo **CLEAR** for **ComputationalLiErAry Repository**. In the beginning we will work with the ADL (Archive of Danish Literature) collection [here](https://drive.google.com/drive/folders/0B8ayHJtV5qOMWjQyVXlsd3pBT2c?usp=sharing), because we have it. Importantly we do *not* have the rights to share the publicly yet (we just scraped their site). Mads is currently negotiating with DSL/Royal Library.

We have one mantra only: *if in doubt, ask*. Bad communication ruins more projects than lack of skills.

## Line ##
- Make a free account at [GitHub](https://github.com/) and forward username to KLN.   
- Install [git](https://git-for-windows.github.io/) for windows and learn to use Git BASH.  
- Run through [GitHub Bootcamp](https://help.github.com/articles/set-up-git/#platform-windows) for windows.  
- Use a [tutorial](http://rogerdudler.github.io/git-guide/) to get used to the git version control system. I suggest that you set up a test repository on you own account and add a couple of files from our collections.   
- Make a new folder in the 'xml_lb' called  'xml_meta' and transfer all metadata files from the 'xml' folder to the new folder (xml metadata has the '-etext-workdb.xml' ending).
- **CLEAR repo reorganization**
	1. each data source e.g. ADL or LB should have
		- a parent folder named by initials, e.g., CLEAR/ADL
			- each parent folder should contain two data folders for markup (xml) and plain text (txt) respectively, e.g., CLEAR/ADL/markup and CLEAR/ADL/plain
			- each parent folder should also contain a metadata folder, e.g.,  CLEAR/ADL/metadata
			- each parent folder should also contain a documentation markdown file with information about the provider, e.g., CLEAR/ADL/provider_ADL.md
			- whenever possible transfer relevant data to folders, e.g., all txt files from ADL to CLEAR/ADL/plain
	2. tools parent folder (CLEAR/tools) for all scripts with subfolders
		- import_export, i.e., CLEAR/tools/import_export
		- preprocessing
		- basic_mdl
		- advanced_mdl
	3. a internal parent folder (CLEAR/internal) for all our mess (including tasklist.md)
	4. important README should stay in CLEAR folder
- **draft documentation markdown file**
	- we need a documentation markdown file with information about the provider for each data collection. Every provider has different needs, but go to their website and copy basic information
	i.e., url, contact information, and license agreement
- **extensive documentation and testing**
	- test users asked for extensive instruction (tutorial-like) for each script we add. I started drafting an example (LINK HERE) for exporting an ADL corpus. Each time we add a script, please write a step by step instruction on how to use i in a similar style  
	- while making the instructions, write down any error or otherwise that you might spot and add them to Zehui's task list.

## Zehui ##
- Clone CLEAR  
- Upload all plain text files from the [ADL Drive](https://drive.google.com/drive/folders/0B8ayHJtV5qOMWjQyVXlsd3pBT2c?usp=sharing) folder to data_adl in CLEAR.  
- Upload ADL_metadata.txt (tab delim, utf-8) file to CLEAR main folder.  
- Write a query script in R or Python that when CLEAR is cloned locally allows the user to generate a corpus for a specific author (all texts by an author author in data_adl) in a new folder by inputting the author's surname (first name in third column of ADL_metadata).
- Work on a xml2txt script (see xml2txt.md for a spaghetti example)
**functions in preprocessing module**  
1: tokenization in uni- to n-grams, a function that tokenize a string into words and multi-word strings, e.g.,

```python
>>> s = 'this is a string'
>>> tokenizer(s) # default size = 1
['this', 'is', 'a', 'string']

>>> tokenizer(s,2)
['this is', 'is a', 'a string']

>>> tokenizer(s,3)
['this is a', 'is a string']

>>> tokenizer(s,4)
['this is a string']
```

2: removal of non-alphanumeric characters with regex, a function that removes non non-alphanumeric characters based on *re*, e.g.,

```python
>>> s = 'this is f@*cking cool!!!'
>>> print re_nalpha(s)
'this is fcking cool'
```

3: basic rule-based and language-specific stemmer,

```python
from nltk.stem.snowball import SnowballStemmer
def stem_list(docstoken, lang = 'english'):
	stemmer = SnowballStemmer(lang, ignore_stopwords = True)
    docsstem = [[stemmer.stem(w) for w in token] for token in docstoken]
    return docsstem
```

4: lemmatization, function for using WordNet's lemmatizer with specific language on tokenized list (unigrams), (some spaghetti that you can use, notice that we need to translate Treebank tags to WordNet in order to get word class, otherwise the lemmatizer would treat all words as nouns)

```python
## lemmatize with NLTK & POS tags from WordNet
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
# change from treebank to wordnet POS tags
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN# noun is baseline
# lemmatize
def vanilla_lemmatizer(unigrams):
    wordnet_lemmatizer = WordNetLemmatizer()
    unigrams_lemma = unigrams
    for i, _ in enumerate(unigrams):# loop over docs
        tmp = pos_tag(unigrams[i])
        for ii, _ in enumerate(tmp):# loop over tokens
            unigrams_lemma[i][ii] = wordnet_lemmatizer.lemmatize(tmp[ii][0],get_wordnet_pos(tmp[ii][1]))
    return unigrams_lemma

```

**functions in basic_stats module**

1: Word frequency dictionary, function that generates a dictionary with word: word frequency mapping for a string and a list of strings

```python
>>> s = 'a rose is a rose is a rose!'
>>> wfreq(s)
{'a': 3, 'rose': 3, 'is': 2}
>>> l = [['a rose is a rose is a rose'],['and a stone is a stone']]
>>> wfreqs(l)
{'a': 5, 'rose': 3, 'is': 3, 'and': 1, 'stone': 2}
```

2: stoplist generation, function that export the top *n* most frequent words to a string or list of strings to a comma-separated txt called *stopwords_n.txt* where n is the number of words in the file

```python
>>> l = [['a rose is a rose is a rose'],['and a stone is a stone']]
>>> gen_stopwords(l,3)
# writes "a, is, rose", notice that when there are draws, both 'is' and 'rose' have a frequency of 3, both/all draw words are written to the file, so
>>> gen_stopwords(l,2)
# is the same as gen_stopwords(l,3) in this case
```

**functions in information_retrieval module**  
1: Document term matrix in list, function that generate a matrix with term frequencies, where rows represent documents and columns words alphabetically sorted. Use list type, not numpy array. The function should also generate a list with the lexicon/column names

```python
>>> l = [['a rose is a rose is a rose'],['and a stone is a stone']]
>>> vspc, lex = dtm(l)
>>> print vspc
[[3,0,2,3,0],[2,1,1,0,2]]
>>> print lex
['a','and','is','rose','stone']
```


## Line & Zehui ##
1. Always document your progress in documentation.md in CLEAR
2. If you are not used to Markdown, might as well learn it with [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Every document we have on git that is not plain text, metadata or code, is written in Markdown. I will recommed the [Atom](https://atom.io/) text editor, which has preview for Markdown.  

## Resources ##

Danish literature from [ADL](http://adl.dk/adl_pub/forside/cv/forside.xsql?nnoc=adl_pub)  
Swedish literature from [Litteraturbanken](http://litteraturbanken.se/#!/start)
