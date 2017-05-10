#coding=utf-8
from xml.sax.handler import ContentHandler
import xml.sax
import sys,os,string
class textHandler(ContentHandler):
    def characters(self, ch):
        sys.stdout.write(ch.encode("UTF-8"))
##this function will take two arguments, one is the source_folder containing all the xml file
##the other is the destination directory you use to store the output text
def convert_to_text(source_file,des_file=os.getcwd()):
	parser = xml.sax.make_parser()
	handler = textHandler()
	parser.setContentHandler(handler)
	file_list = os.listdir(source_file)
	print (file_list)

	##these three lines creates an folder called txt within txt_output in the des_file
	##if not specified, it will be created within the current working directory
	os.chdir(des_file);
	os.mkdir("txt_output");
	des_pos=os.path.join(des_file,"txt_output")
	os.chdir(des_pos)
	for filename in file_list:
		filepath = os.path.join(source_file,filename)
		print filepath
		parser.parse(filepath)
		temp = string.replace(filename,".xml",".txt")
		des_file_temp = os.path.join(des_pos,temp)
		orig_stdout = sys.stdout
		f = file(des_file_temp, 'w')
		sys.stdout = f
		parser.parse(filepath)
		sys.stdout = orig_stdout
		f.close()
## use sigal quote to type in the source dir and destination dir in as command line arguments 'F:\2017\scan_modern\TEST2\GV\markup'
if __name__=='__main__':
	if (len(sys.argv)==3):
		convert_to_text(sys.argv[1],sys.argv[2])
	elif(len(sys.argv)==2):
		convert_to_text(sys.argv[1])
	else:
		print("Invalid input argumnets")