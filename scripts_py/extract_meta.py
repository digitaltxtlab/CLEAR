import os, sys, shutil, string, re
from xml.etree import ElementTree as ET
reload(sys)
sys.setdefaultencoding('utf-8')
###description
# this script is used to extract Metadata from the xml files
# after running this scripts we could get an folder called "data_from_xml" appearing in the MAIN directory of CLEAR
# which will contain a file called 'metadata.txt'
# 'metadata.txt' is a combination of  the xml files under the dir of xml_lb/xml_meta 
###how to use
# >	usage:	keep this script in the current folder, use command line terminal "cd"
#			to this directory (scripts_py)
#			then run this script(type in "python extract_meta.py")
###the content of the metadata
#	each row contain the following information:
# 	authorid,	lbworkid, 	tittle,	tittleid,	imprintyear,	language
#	which is seperated by ","




def extractMetadata():
	cwd=os.getcwd()
	parent_path = os.path.dirname(cwd)
	des_dir=parent_path+"\\"+"xml_lb"+ "\\" + "xml_meta"
	file_list=os.listdir(des_dir)
	os.chdir(des_dir)
	msg = ""
	
	for file_name in file_list:
		tree = ET.parse(file_name)
		for root in tree.findall('.//authorid'):
			msg = msg + root.text
			msg = msg + ",	"
		for root in tree.findall('.//lbworkid'):
			msg = msg + root.text
			msg = msg + ",	"
		for root in tree.findall('./title'):
			msg = msg + root.text
			msg = msg + ",	"
		for root in tree.findall('./titleid'):
			msg = msg + root.text
			msg = msg + ",	"			
		for root in tree.findall('.//imprintyear'):
			msg = msg + root.text
			msg = msg + ",	"	
		for root in tree.findall('.//language'):
			msg = msg + root.text
			msg = msg + ",	"	
		msg = msg + "\n"
	os.chdir(parent_path)
	os.mkdir("data_from_xml")
	des_dir="data_from_xml"+ "\\" + "metadata.txt"
	file = open(des_dir,'w')
	file.write(msg)
	file.close()
	
if __name__=='__main__':
	extractMetadata()