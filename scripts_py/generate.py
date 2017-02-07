import os, sys, shutil, string, re
#this script is used to get all the files written by a certain author
#you can do so by typing in the name of the author and run this script,
#the author name is the third column of the metadata 

# >	usage: keep this script in the current folder, use command line terminal "cd"
#          to this directory (scripts_py), run this script with python and the author you want to find
#          here is an example: python generate.py Nansen
#          then you can get a folder containing the corresponding files appearing in the "main directory" of CLEAR 

# before running this script, please go through following points:
# > this script is designed to be used on windows platform,
#   if you want to run this script on ios, please try to change the directory form
# > please don't change the directory structure of "CLEAR"
#	Just keep it the same as you clone it - the change of the dir structure could 
# 	lead to the failure of the scripts 

# use the file_list generate by second function
# this function can copy all the files and put them in a new folder 
def creat_corpus(corpus_name,file_list):
	cwd=os.getcwd()
	parent_path = os.path.dirname(cwd)
	os.chdir(parent_path)
	os.mkdir(corpus_name)
	des_dir=parent_path	+"\\"+ corpus_name
	working_dir=parent_path + "\\"+ "data_adl"	
	os.chdir(working_dir)
	for file_name in file_list:
		shutil.copy(file_name,des_dir)

		
# this function will search through the ADL_metadata and 
# return a file list of all the corresponding file			
def	creat_file_list(author_name):
	file_list=['non']
	cwd=os.getcwd()
	parent_path = os.path.dirname(cwd)
	des_pos=parent_path+"\\"+"ADL_metadata.txt"
	fh=open(des_pos)
	for line in fh.readlines():
		L=string.split(line)
		if(re.search(author_name,L[2])):
			temp_string=L[0]+"_"+L[1]+".txt"
			file_list.append(temp_string)
	return file_list[1:]
	
if __name__=='__main__':
	#author_name= "Blicher"
	author_name= sys.argv[1]
	file_list=creat_file_list(author_name)	#	get	file list 
	
	corpus_name=string.replace(file_list[1],".txt","_")	#	create the new folder's name using an unique id
	corpus_name+=author_name[0]	# the form of this id is like this "numbers_numbers_charecter", eg. 13_789_B
	
	creat_corpus(corpus_name,file_list)		#	put all the needed files to new folder