# Documentation #

File for more detailed progress description (Line & Zehui primarily)

---
2/2/2017 - Zehui

Cloning CLEAR to local computer

Add metadata to **main directory** (locally)

Add plain text files to **data_adl dir** (locally)

***
2/3/2017 - Zehui

Push the local changes to remote repository

---
2/7/2017 - Zehui

Creat python scripts used to **generate corpus** and push the changes

to remote repository

---
3/5/2017 - Line

Create folder **xml_meta** inside **xml_lb**

Move  metadata from **xml** to **xml_meta**

---
3/6/2017

Add two python scripts to scripts_py,

which is used to convert file from **xml** to **txt**

---
3/8/2017 - Line

Run python script generate.py on pc,

seems to work, except with authors whose surnames contain æ, ø and å:
~~~
$ python generate.py Hjortø
Traceback (most recent call last):
  File "generate.py", line 52, in <module>
    corpus_name=string.replace(file_list[1],".txt","_") #       create the new folder's name using an unique id
IndexError: list index out of range
~~~

Also possibly a problem with extracting all files from authors,

for example generating a Kingo folder gives 635 files, while searching

for Kingo in ADL_metadata.txt gives 640 hits.

---
3/13/2017
generate.py is OS dependent (written for windows path), need to scale for unix systems (example of OS independent: )

---
added demotools for yes, tools that we want to demonstrated

---
3/29/2017
Repo reorganization.

Make parent folders for each data source, each containing a folder for plain, markup and metadata.

Make parent folder for tools containing scrips.

Make internal folder for e.g. tasklist.md, documetation.md and mess.

---
3/30/2017
Add provider documentation markdown files containing basic information on each data provider in the parent folders for ADL, BSL, GV and LB.

---
4/2/2017 - Zehui

Add preprocessing module, tokenizer and re_nalpha is within it

Plan for the last couple of weeks:

1.try to work on  **basic_stats module**

2.go back to **generate.py, extract_text.py and extract_meta.py**

---
4/8/2017 - Zehui

Finish  **basic_stats module**

Plan for the future

1.try to work on **information_retrieval module**

2.modify **generate.py, extract_text.py and extract_meta.py**

---
4/23/2017 - Line

Add comments and more examples to tutorial.md

Rename tutorial.md to cmd_generate.md and move it to CLEAR/tutorials
---
4/24/2017 - Zehui

Fix the behaviour of n-gram tokenizer in preprocessing module
