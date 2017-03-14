# Tasks in CLEAR #

First of all, thank you for joining the project, looking forward to working with you. We have dubbed the repo **CLEAR** for **ComputationalLiErAry Repository**. In the beginning we will work with the ADL (Archive of Danish Literature) collection [here](https://drive.google.com/drive/folders/0B8ayHJtV5qOMWjQyVXlsd3pBT2c?usp=sharing), because we have it. Importantly we do *not* have the rights to share the publicly yet (we just scraped their site). Mads is currently negotiating with DSL/Royal Library.

We have one mantra only: *if in doubt, ask*. Bad communication ruins more projects than lack of skills.

## Line ##
1. Make a free account at [GitHub](https://github.com/) and forward username to KLN.   
2. Install [git](https://git-for-windows.github.io/) for windows and learn to use Git BASH.  
3. Run through [GitHub Bootcamp](https://help.github.com/articles/set-up-git/#platform-windows) for windows.  
4. Use a [tutorial](http://rogerdudler.github.io/git-guide/) to get used to the git version control system. I suggest that you set up a test repository on you own account and add a couple of files from our collections.   
5. Make a new folder in the 'xml_lb' called  'xml_meta' and transfer all metadata files from the 'xml' folder to the new folder (xml metadata has the '-etext-workdb.xml' ending).


## Zehui ##
1. Clone CLEAR  
2. Upload all plain text files from the [ADL Drive](https://drive.google.com/drive/folders/0B8ayHJtV5qOMWjQyVXlsd3pBT2c?usp=sharing) folder to data_adl in CLEAR.  
3. Upload ADL_metadata.txt (tab delim, utf-8) file to CLEAR main folder.  
4. Write a query script in R or Python that when CLEAR is cloned locally allows the user to generate a corpus for a specific author (all texts by an author author in data_adl) in a new folder by inputting the author's surname (first name in third column of ADL_metadata).
5. Work on a xml2txt script (see xml2txt.md for a spaghetti example)

## Line & Zehui ##
1. Always document your progress in documentation.md in CLEAR
2. If you are not used to Markdown, might as well learn it with [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Every document we have on git that is not plain text, metadata or code, is written in Markdown. I will recommed the [Atom](https://atom.io/) text editor, which has preview for Markdown.  

## Resources ##

Danish literature from [ADL](http://adl.dk/adl_pub/forside/cv/forside.xsql?nnoc=adl_pub)  
Swedish literature from [Litteraturbanken](http://litteraturbanken.se/#!/start)
