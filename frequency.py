""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	text = f.read()
	(before,text) = text.split('START OF THIS PROJECT GUTENBERG EBOOK')
	text = text.translate(None,string.punctuation)
	text = text.lower()
	return text.split()

def get_word_histogram(word_list):
	hist = dict()
	for word in word_list:
		hist[word] = hist.get(word,0)+1;
	return hist

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	hist = get_word_histogram(word_list)
	histlist = hist.items()
	sorted_hist = sorted(histlist, key = lambda tuple: tuple[1])
	sorted_hist = sorted_hist[::-1]
	i = 0
	sorted_list = []
	while i < n:
		sorted_list.append(sorted_hist[i][0])
		i = i + 1
	return sorted_list

word_list = get_word_list('davidcopperfield.txt')
sorted_list =  get_top_n_words(word_list,100)
print sorted_list
