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
3/19/2017
Repo reorganization. 

Make parent folders for each data source, each containing a folder for plain, markup and metadata.

Make parent folder for tools containing scrips.

Make internal folder for e.g. tasklist.md, documetation.md and mess.
