from itertools import combinations
from itertools import permutations
import cProfile
import hashlib
import sys
import time

############# DECLARATION OF CONSTANTS #############

ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_SORTED = ''.join(sorted(ANAGRAM)).strip()+"~"
ANAGRAM_LET_DICT = {}

for letter in ANAGRAM_SORTED:
	if(letter in ANAGRAM_LET_DICT):
		ANAGRAM_LET_DICT[letter] += 1
	else:
		ANAGRAM_LET_DICT[letter] = 1 

print ANAGRAM_LET_DICT


ANAGRAM_LETTERS_LENGTH = len(ANAGRAM_SORTED)

HASH_EASY = "e4820b45d2277f3844eac66c903e84be"
HASH_INTERMEDIATE = "23170acc097c24edb98fc5488ab033fe"
HASH_HARD = "665e5bcb0c20062fe8abaaf4628bb154"

WORD_LIST_FILE = "wordlist"

################# HELPER FUNCTIONS #################

# def exists_in_anam(child):

# 	child = sorted(child)

# 	# by sorting we save some time here, we avoid a nested loop
# 	i = 0
# 	for letter in child:

# 		while i < ANAGRAM_LETTERS_LENGTH:
# 			letter_m = ANAGRAM_SORTED[i]
			
# 			i += 1
# 			if(letter_m > letter):
# 				return False
# 			elif(letter_m == letter):
# 				break
			
# 	return True

def exists_in_anam(child):

	anag_dict = dict(ANAGRAM_LET_DICT)

	for letter in child:
		if letter not in anag_dict:
			return False
		else:
			if(anag_dict[letter] < 1):
				return False
			else:
				anag_dict[letter] -= 1
			
			
	return True


def combizz(n, r):
	return [" ".join(map(str, comb)) for comb in permutations(n, r)]


################## MAIN FUNCTION ###################

def main():

	start_time = time.time()

	# store words in a set to avoid duplicates.
	# filter out words with letters that are not in the anagram
	word_bag = set()
	for line in open(WORD_LIST_FILE):
		word = line.rstrip('\n')	
		if (word.isalnum() and exists_in_anam(word)):
			word_bag.add(word)


	# sort the word in word_bag by length for efficiency
	word_bag = sorted(word_bag, key=len, reverse=True)


	# calculate the length of each word once and store them in 
	# a dictionary to avoid redundant calls to len() function
	word_len_map = {}
	for word in word_bag:
		word_len_map[word] = len(word)

	
	# build a word->candidates map by finding all possible combination 
	# candidates for each word. e.g. {'straws': ['nulity', 'pointy', ...
	word_bag_len = len(word_bag)
	comb_candids_map = {}
	for index, word in enumerate(word_bag):
		candids = []
		j = index
		while j < word_bag_len:
			poten_candid = word_bag[j]
			phrase = word+poten_candid
			phrase_len = word_len_map[word]+word_len_map[poten_candid]
			# check if the word can be a combination candid.
			# plus 1 is to account for space
			if(phrase_len+1 <= ANAGRAM_LENGTH):
				if(exists_in_anam(phrase)):
					candids.append(poten_candid)

			j += 1

		# map the candidates (if any) to the word
		if(len(candids) > 0):
			comb_candids_map[word] = candids


	# start with 3-word phrases and go up to max no. of words, 
	# which is equal to number of letters we have in the anagram
	phrase_len = 3

	while (phrase_len < ANAGRAM_LETTERS_LENGTH):
		
		print "Searching "+str(phrase_len)+"-word phrases.."

		c = phrase_len - 1
		phrase = [""] * phrase_len

		# take one word at a time and build phrases with it
		# and its candidate
		for word, candids in comb_candids_map.items():

			combs = combinations(candids, c)

			phrase[0] = word

			for cos in combs:

				phrase_length = word_len_map[word]+c
				
				for i, w in enumerate(cos):
					phrase[i+1] = w
					phrase_length += word_len_map[w]

				if(phrase_length == ANAGRAM_LENGTH+(c-2)):				
					if(exists_in_anam("".join(phrase))):
						combo = combizz(phrase, phrase_len)
						for co in combo:
							candid_hash = hashlib.md5(co).hexdigest()
							if(candid_hash == HASH_EASY):
								end_time = time.time()
								print "Easiest Phrase: "+co+" (found in "+str(round(end_time - start_time, 2))+" secs)"
							elif(candid_hash == HASH_INTERMEDIATE):
								end_time = time.time()
								print "Hard Phrase: "+co+" (found in "+str(round(end_time - start_time, 2))+" secs)"
							elif(candid_hash == HASH_HARD):
								end_time = time.time()
								print "Hardest Phrase: "+co+" (found in "+str(round(end_time - start_time, 2))+" secs)"
								sys.exit()

		phrase_len += 1
	

if __name__ == "__main__":
    cProfile.run('main()')


