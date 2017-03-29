#coding=utf-8
from xml.sax.handler import ContentHandler
import xml.sax
import sys,os,string
class textHandler(ContentHandler):
    def characters(self, ch):
        sys.stdout.write(ch.encode("UTF-8"))


parser = xml.sax.make_parser()
handler = textHandler()
parser.setContentHandler(handler)

cwd=os.getcwd()
parent_path = os.path.dirname(cwd)
working_path = parent_path + "\\" +"xml_lb"+"\\"+"xml"
file_list = os.listdir(working_path)

##these three lines creates an folder called txt within xml_lb
working_dir = parent_path + "\\" +"xml_lb"
os.chdir(working_dir)
os.mkdir("txt")
##ignore if there have already existed xml_lb\txt
for filename in file_list:
	filepath = working_path + "\\" + filename
	parser.parse(filepath)

	temp = string.replace(filename,".xml",".txt")
	des_file = parent_path + "\\" + "xml_lb" + "\\"+"txt"+"\\"+temp

	orig_stdout = sys.stdout
	f = file(des_file, 'w')
	sys.stdout = f
	parser.parse(filepath)
	sys.stdout = orig_stdout
	f.close()
 