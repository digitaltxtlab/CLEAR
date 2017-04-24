#coding=utf-8
import re
from nltk.tokenize import word_tokenize

##removes non non-alphanumeric characters based on re
def re_nalpha(str):
	pattern = re.compile(r'[^\w\s]', re.U)
	return re.sub(r'_', '', re.sub(pattern, '', str))

##tokenization in uni- to n-grams,a function that tokenize a string into words and multi-word strings
#please be aware of that the redundant words will be  append to the the end as one gram string
#this fucntion will return a list containing the tokenized strings
def tokenizer(text,size=1):
	# tokenize to 1 gram strings
	result_size1 = word_tokenize(text)
	if size == 1:
		return result_size1
	# tokenize into n gram strings
	else:
		temp_list = []
		temp_size = 0
		for i in range(0,len(result_size1)-size+1):
			temp_str=''
			for j in range(size):
				temp_str = temp_str+" "+ result_size1[temp_size+j]
			temp_list.append(temp_str[1:])
			temp_size += 1
		return temp_list

#this is a test, please remove if not needed
s = 'you looks so great and so beautiful'
print tokenizer(s,3)
#s = 'this is f@*cking cool!!!'
#print re_nalpha(s)
