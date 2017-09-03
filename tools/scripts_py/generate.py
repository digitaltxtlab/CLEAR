#coding=utf-8
import os, sys, shutil, string, re
import codecs
#this script is used to get all the files written by a certain author
#you can do so by typing in the name of the author and run this script,
#the author name is the third column of the metadata 

# >	usage: keep this script in the current folder, use command line terminal "cd"
#          to this directory (scripts_py), run this script with python and the author you want to find
#          here is an example: python generate.py Nansen
#          then you can get a folder containing the corresponding files appearing in the "main directory" of CLEAR 

# before running this script, please go through following points:
# > please note that if the authors' surnames contain æ, ø ,ë and å
#	try to type in the author's name manually below instead of typing it in the terminal
# > please don't change the directory structure of "CLEAR"
#	Just keep it the same as you clone it - the change of the dir structure could 
# 	lead to the failure of the scripts 

# use the file_list generate by second function
# this function can copy all the files and put them in a new folder 
def creat_corpus(corpus_name,file_list):
	cwd=os.getcwd()
	parent_path = os.path.dirname(os.path.dirname(cwd))
	os.chdir(parent_path)
	os.mkdir(corpus_name)
	des_dir=os.path.join(parent_path,corpus_name)
	working_dir=os.path.join(parent_path,"ADL","plain")	
	os.chdir(working_dir)
	for file_name in file_list:
		shutil.copy(file_name,des_dir)

		
# this function will search through the ADL_metadata and 
# return a file list of all the corresponding file			
def	creat_file_list(author_name):
	file_list=['non']
	cwd=os.getcwd()
	parent_path = os.path.dirname(os.path.dirname(cwd))
	des_pos=os.path.join(parent_path,"ADL","metadata","ADL_metadata.txt")
	fh=codecs.open(des_pos)
	for line in fh.readlines():
		L=string.split(line)
		if(re.search(author_name,L[2])):
			temp_string=L[0]+"_"+L[1]+".txt"
			file_list.append(temp_string)
	return file_list[1:]
def create_multiple_corpus(list_author_name):
    for author_name in list_author_name:
        file_list=creat_file_list(author_name)	#	get	file list 
        corpus_name=string.replace(file_list[1],".txt","_")	#	create the new folder's name using an unique id
        corpus_name+=author_name[0]	# the form of this id is like this "numbers_numbers_charecter", eg. 13_789_B
        creat_corpus(corpus_name,file_list)		#	put all the needed files to new folder
if __name__=='__main__':
	#append the user's name to the end of sys.argv if authors' surnames contain æ, ø ,ë and å 
	# e.g. sys.argv.append("Aakjær")
    list_author_name= sys.argv[1:]
    create_multiple_corpus(list_author_name)