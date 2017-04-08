from preprocessing import tokenizer
from preprocessing import re_nalpha
## Word frequency dictionary,function that generates a dictionary with word: 
## word frequency mapping for a string or a list of strings
def wfreq (text):
	word_dic = {}
	if isinstance(text,str):
		#preprocessing module is used to tokenize the text
		text = tokenizer(re_nalpha(text))
		for word in text:
			if word not in word_dic:
				word_dic[word] = 1
			else:
				word_dic[word] +=1
	else:
		for sent in text:
			sent_str = tokenizer(re_nalpha(sent[0]))
			for word in sent_str:
				if word not in word_dic:
					word_dic[word] = 1
				else:
					word_dic[word] +=1
	return  word_dic
	
##stoplist generation, this function will generate a file called stopwords_n.txt in wording dir
##from a string or a list of strings
#if n is bigger than the lenth of the dictionary return all the words as stoplist
def gen_stopwords(text,n):
	print_str = ''
	fre_dic = wfreq(text)
	sorted_string = sorted(fre_dic.items(), key=lambda d: d[1],reverse=True)
	if n>len(fre_dic):
		n = len(fre_dic)
	for index in range(n):
		print_str += ","+ sorted_string[index][0]
	file_name = r'./stopwords_n.txt'
	with open(file_name, 'wb') as x_file:
		x_file.write(print_str[1:])
	
	
	
	
##this is a test, please remove if not needed 

# test for wfreq
s = 'a rose is a rose is a rose!'
print wfreq(s)

l = [['a rose is a rose is a rose'],['and a stone is a stone']]
print wfreq(l)

#test for gen_stopwords
gen_stopwords(s,4)


