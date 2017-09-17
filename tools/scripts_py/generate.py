#cod#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os, sys, shutil, string, re
import codecs
#this script is used to get all the files written by a certain author or authors
#you can do so by typing in the name(surname or full name) of the author and run this script,
#the author's full name is the second column of the metadata

# >	usage: keep this script in the current folder, use command line terminal "cd"
#          to this directory (scripts_py), run this script with python and the author(or multiple authors) you want to find
#          here is an example: python generate.py Grundtvig
#          then you can get a folder containing the corresponding files appearing in the "main directory" of CLEAR
#          exmple for multiple users: python generate.py N.F.S. Grundtvig, Helge Rode

# before running this script, please go through following points:
# > please note that if the authors' names contain æ, ø ,ë and å
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
	des_pos=os.path.join(parent_path,"ADL","metadata","metadata_adl.csv")
	fh=codecs.open(des_pos)
	if len(string.split(author_name))==1:
		for line in fh.readlines():
			L=string.split(line,',')
			if(re.match(author_name,string.split(L[1])[-1])):
				temp_string=L[0]+".txt"
				file_list.append(temp_string)
	else:
		for line in fh.readlines():
			L=string.split(line,',')
			if(author_name==L[1].lstrip()):
				temp_string=L[0]+".txt"
				file_list.append(temp_string)
	return file_list[1:]
def create_multiple_corpus(list_author_name):
    for author_name in list_author_name:
        file_list=creat_file_list(author_name)	#	get	file list
        corpus_name=string.replace(file_list[1],".txt","_")	#	create the new folder's name using an unique id
        corpus_name+=author_name[0]	# the form of this id is like this "numbers_numbers_charecter", eg. 13_789_B
        creat_corpus(corpus_name,file_list)		#	put all the needed files to new folder
def name_decoder(name_list):
    temp_string = ''
    for index in name_list:
        temp_string += index + " "
    temp_list = string.split(temp_string,',')
    return_list = list() 
    for author in temp_list:
        return_list.append(author.lstrip().rstrip())
    return return_list
        
    
if __name__=='__main__':
	#append the user's name to the end of sys.argv if authors' names contain æ, ø ,ë and å
	# e.g. sys.argv.append("Aakjær")
    list_author_name = name_decoder(sys.argv[1:])
    create_multiple_corpus(list_author_name)
