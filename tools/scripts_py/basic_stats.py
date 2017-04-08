from preprocessing import tokenizer

## Word frequency dictionary,function that generates a dictionary with word: 
## word frequency mapping for a string or a list of strings
def wfreq (text):
	word_dic = {}
	if isinstance(text,str):
		#preprocessing module is used to tokenize the text
		text = tokenizer(text)	
		for word in text:
			if word not in word_dic:
				word_dic[word] = 1
			else:
				word_dic[word] +=1
	else:
		for sent in text:
			sent_str = tokenizer(sent.pop())
			for word in sent_str:
				if word not in word_dic:
					word_dic[word] = 1
				else:
					word_dic[word] +=1
		print "I am there"
	return  word_dic
	
#this is a test, please remove if not needed 
#input is a string
s = 'a rose is a rose is a rose!'
print wfreq(s)
#input is a list of string
l = [['a rose is a rose is a rose'],['and a stone is a stone']]
print wfreq(l)
