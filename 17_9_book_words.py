from collections import defaultdict

def create_freq_lookup(book):
	sentences = book.strip('.').split('.')
	words = []
	for sentence in sentences:
		words.extend(sentence.strip(' ').split(' '))
	
	freq_lookup = defaultdict(lambda: 0)
	for word in words:
		freq_lookup[word.lower()] += 1

	return freq_lookup

book = "The cat in the hat. The cat sat on the mat with the other cats."
freq_lookup = create_freq_lookup(book)
