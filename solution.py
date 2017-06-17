##################### IMPORTS #####################

from itertools import combinations
from itertools import permutations
import hashlib
import sys
import time

############# DECLARATION OF CONSTANTS #############

ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_LETTERS_DICT = {}
for letter in ANAGRAM:
	if(letter in ANAGRAM_LETTERS_DICT):
		ANAGRAM_LETTERS_DICT[letter] += 1
	else:
		ANAGRAM_LETTERS_DICT[letter] = 1 
HASHES = {
	"Easiest ": "e4820b45d2277f3844eac66c903e84be",
	"Moderate": "23170acc097c24edb98fc5488ab033fe",
	"Hardest ": "665e5bcb0c20062fe8abaaf4628bb154"
}
HASHES_LEN = len(HASHES)
WORD_LIST_FILE = "wordlist"

##################### GLOBALS ######################

targets_found = 0

################# HELPER FUNCTIONS #################

def is_anagram(child):

	""" is_anagram checks if a given string only consists of the letters in 
	ANAGRAM. Returns True if the string is part of the anagram, False otherwise
    """

	anag_dict = dict(ANAGRAM_LETTERS_DICT)

	for letter in child:
		if letter not in anag_dict:
			return False
		else:
			if(anag_dict[letter] < 1):
				return False
			else:
				anag_dict[letter] -= 1
	
	return True


def permute_words(n, r):

	""" takes a list of words and computes all posible permutations of the 
	words in the string seperated by spaces. E.g. it receives ['a','b',..] and 
	returns ['a b', 'b a',...] 
    """

	return [" ".join(map(str, comb)) for comb in permutations(n, r)]


def filter_words(words):
	
	""" takes a set of words and filters out the ones with letters not in 
	anagram.
	"""

	word_bag = set()
	for line in words:
		word = line.rstrip('\n')	
		if (is_anagram(word)):
			word_bag.add(word)

	return word_bag


def build_word_candids_map(word_bag, word_len_map):
	
	""" takes a set of words and for every given word, finds all candids that
	can be in a phrase with that word. In that way, it builds a 
	word->candidates map. E.g. {'straws': ['nulity', 'pointy', ...],...}
	"""

	word_bag_len = len(word_bag)
	word_candids_map = {}
	for index, word in enumerate(word_bag):
		candids = []
		j = index
		while j < word_bag_len:
			poten_candid = word_bag[j]
			phrase = word+poten_candid
			phrase_len = word_len_map[word]+word_len_map[poten_candid]
			# plus 1 is to account for space
			if(phrase_len+1 <= ANAGRAM_LENGTH):
				if(is_anagram(phrase)):
					candids.append(poten_candid)

			j += 1

		# map the candidates (if any) to the word
		if(len(candids) > 0):
			word_candids_map[word] = candids

	return word_candids_map

def check_hash(phrase, start_time):

	""" takes a phrase and checks if it is on the phrases we are looking for
	"""

	phrase_hash = hashlib.md5(phrase).hexdigest()

	for key, target in HASHES.items():
		if(phrase_hash == target):
			end_time = time.time()
			elapsed = str(round(end_time - start_time, 2))
			print key+" phrase:\t"+phrase+" \t(found in "+elapsed+" secs)"
			# increment phrases found so far
			global targets_found
			targets_found += 1
	

def search_for_phrases(word_candids_map, phrase_len, word_len_map, start_time):

	""" builds phrases of certain length using word_candids_map and check if 
	the phrase is one of the phrases we are looking for.
	"""

	candid_comb_len = phrase_len - 1
	phrase = [""] * phrase_len

	# take one word at a time and build phrases with it and different 
	# combination of its candidates
	for word, candids in word_candids_map.items():

		candid_combos = combinations(candids, candid_comb_len)
		phrase[0] = word

		for combo in candid_combos:

			# build up the phrase and calculate its length
			phrase_length = word_len_map[word]+candid_comb_len
			for i, w in enumerate(combo):
				phrase[i+1] = w
				phrase_length += word_len_map[w]

			if(phrase_length == ANAGRAM_LENGTH+(candid_comb_len-2)):
				# check if the phrase built can be an anagram			
				if(is_anagram("".join(phrase))):
					# look at all the different arrangement of words in phrase
					phrase_permuts = permute_words(phrase, phrase_len)
					for maybe_the_one in phrase_permuts:
						check_hash(maybe_the_one, start_time)
						# let the caller know when all the phrases are found
						if(targets_found == HASHES_LEN):
							return True

	# tell the caller that there are still phrases to find
	return False
################## MAIN FUNCTIONS ##################

def main():

	""" this is where it all begins
	"""

	# save the starting time
	start_time = time.time()

	# read the words
	print "Reading words..."
	word_bag = open(WORD_LIST_FILE)

	# filter out words with letters not in the anagram
	print "Filtering words..."
	word_bag = filter_words(word_bag)

	# sort the words by length for efficiency
	word_bag = sorted(word_bag, key=len, reverse=True)

	# store length of each word to avoid redundant calls to len()
	word_len_map = {}
	for word in word_bag:
		word_len_map[word] = len(word)

	# build a word->candidates map by finding all possible combination 
	# candidates for every word
	word_candids_map = build_word_candids_map(word_bag, word_len_map)

	# search 3-word phrases, then 4-word phrases and so on
	phrase_len = 3
	while (phrase_len < ANAGRAM_LENGTH):
		
		print "Searching "+str(phrase_len)+"-word phrases..."
		its_over = search_for_phrases(word_candids_map, phrase_len, 
										word_len_map, start_time)

		# end this maddness as soon as all the hashes are found
		if(its_over):
			return

		phrase_len += 1
	

if __name__ == "__main__":
    main()


