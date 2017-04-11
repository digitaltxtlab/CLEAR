from basic_stats import wfreq
## this function will take a list of list, and each sub list contain a string 
## and generate a matrix with term frequencies
def dtm(input_list):
	lex_list = wfreq(input_list).keys()
	vspc_list = []
	for string in input_list:
		temp_num = 0
		string_dict = wfreq(string[0])
		vspc_temp_list = []
		for overall_word in lex_list:
			if overall_word in string_dict:
				temp_num = string_dict[overall_word]
			vspc_temp_list.append(temp_num)
			temp_num=0
		vspc_list.append(vspc_temp_list)
	return vspc_list,lex_list

##this is the test module for dtm,please remove if not used
#l = [['a rose is a rose is a rose'],['and a stone is a stone']]
#vspc,lex = dtm(l)
#print vspc
#print lex
