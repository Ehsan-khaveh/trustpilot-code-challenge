import hashlib
import cProfile
import itertools
from itertools import permutations
import sys

############# DECLARATION OF CONSTANTS #############

ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_SORTED = ''.join(sorted(ANAGRAM)).strip()+"~"
ANAGRAM_LETTERS_LENGTH = len(ANAGRAM_SORTED)
# ANAGRAM_HASH = hashlib.md5(ANAGRAM).hexdigest()

HASH_EASY = "e4820b45d2277f3844eac66c903e84be"
#easy string = "printout stout yawls"
HASH_INTERMEDIATE = "23170acc097c24edb98fc5488ab033fe"
HASH_HARD = "665e5bcb0c20062fe8abaaf4628bb154"
 #easy string = "wu lisp not statutory"

WORD_LIST_FILE = "wordlist"

L = 0

################# HELPER FUNCTIONS #################

def exists_in_anam(child):

	child = sorted(child)

	# by sorting we save some time here, we avoid a nested loop
	i = 0
	for letter in child:

		while i < ANAGRAM_LETTERS_LENGTH:
			letter_m = ANAGRAM_SORTED[i]
			
			i += 1
			if(letter_m > letter):
				return False
			elif(letter_m == letter):
				break
			
	return True

def combs(n, r):
	return [" ".join(map(str, comb)) for comb in permutations(n, r)]
	
def main():

	# store the word list in a set. 
	# in this way we avoid duplicates
	word_bag = set()
	for line in open(WORD_LIST_FILE):
		word = line.rstrip('\n')
		# filter out words that have letters which are not in the anagram
		if (word.isalnum() and exists_in_anam(word)):
			word_bag.add(word)

	# sort the word in word_bag by length for efficiency (?)
	word_bag = sorted(word_bag, key=len, reverse=True)

	# calculate the length of each word and store them in a dictionary
	# to avoid redundant calls to len() function
	word_len_map = {}
	for word in word_bag:
		word_len_map[word] = len(word)
	
	# for every word, go through the  get all possible combination candidates
	# for every word in the filtered list
	word_bag_len = len(word_bag)
	comb_candids_map = {}
	for index, word in enumerate(word_bag):
		# for each word, loop through all the words appearing after 
		# it in the sorted set and choose candids from them
		candids = []
		j = index
		while j < word_bag_len:
			next_word = word_bag[j]
			phrase = word+next_word
			phrase_len = word_len_map[word]+word_len_map[next_word]
			# check if the word can be a combination candid.
			# plus 1 is to account for space
			if(phrase_len+1 <= ANAGRAM_LENGTH):
				if(exists_in_anam(phrase)):
					candids.append(next_word)

			j += 1

		# store the candids found for this word in the dictionary
		if(len(candids) > 0):
			comb_candids_map[word] = candids


	r = 3

	counter = 0

	list_of_l = []
	phrase = [""] * r
	for key, candids in comb_candids_map.items():
		n = len(candids)
		if(r > n):
			continue
		indices = range(r-1)
		phrase[0] = key
		c = r-1
		c_range = list(reversed(range(c)))
		while(True):

			# check if we have looked at all the combinations
			for i in c_range:
				if indices[i] != i + n - c:
					break
			else:
				break


			# Update the indices
			indices[i] += 1
			j = i+1
			while (j<c):
				indices[j] = indices[j-1] + 1
				j += 1


			# Fill up the phrase array based on updated indices
			phrase_length = word_len_map[phrase[0]] + c
			for k, i in enumerate(indices):
				word = candids[i]
				phrase[k+1] = word
				phrase_length += word_len_map[word]
				

			if(phrase_length == ANAGRAM_LENGTH+(c-2)):
				if(exists_in_anam("".join(phrase))):
					# print phrase
					combo = combs(phrase, r)
					for co in combo:
						candid_hash = hashlib.md5(co).hexdigest()
						if(candid_hash == HASH_EASY):
							print "THIS IS easy => "+co
						elif(candid_hash == HASH_INTERMEDIATE):
							print "THIS IS intermediate => "+co
						elif(candid_hash == HASH_HARD):
							print "THIS IS very hard => "+co
							sys.exit()

		counter += 1
		# print counter

if __name__ == "__main__":
    cProfile.run('main()')


