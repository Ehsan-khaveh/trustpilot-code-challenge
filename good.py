import hashlib
import cProfile
import itertools
from itertools import permutations

############# DECLARATION OF CONSTANTS #############

ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_SORTED = ''.join(sorted(ANAGRAM)).strip()+"~"
ANAGRAM_LETTERS_LENGTH = len(ANAGRAM_SORTED)

HASH_EASY = "e4820b45d2277f3844eac66c903e84be"
#easy string = "printout stout yawls"
HASH_INTERMEDIATE = "23170acc097c24edb98fc5488ab033fe"
HASH_HARD = "665e5bcb0c20062fe8abaaf4628bb154"

LIST_FILE_NAME = "wordlist"

################# HELPER FUNCTIONS #################

def isalphanum(string):
	return string.isalnum()

def quick_sort(string):
	return ''.join(sorted(string))

def exists_in_anam(child):

	child = quick_sort(child)

	if(ANAGRAM_LETTERS_LENGTH < len(child)):
		return False

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

	words_set = set()

	# store the word list in a set 
	# in this way we get rid of duplicates too
	for line in open(LIST_FILE_NAME):
		word = line.rstrip('\n')
		# filter out words that have letters which are not in the anagram
		if (isalphanum(word) and exists_in_anam(word)):
			words_set.add(word)

	# store some constant for reusability
	word_list = list(words_set)
	filtered_len = len(word_list)
	possib_dict = {}

	# get all possible combination candidates for every word in the filtered list
	for ind, word in enumerate(word_list):
		comb_list = []
		j = ind
		while j < filtered_len:
			candid = word_list[j]
			comb = word+candid
			len_comb = len(comb)
			# plus 1 to account for space
			if(len_comb+1 <= ANAGRAM_LENGTH):
				if(exists_in_anam(comb)):
					comb_list.append(candid)
			j += 1

		if(len(comb_list) > 0):
			possib_dict[word] = comb_list

	# build permutations for every word and it's candidates and filter combinations
	list_of_l = []
	build = [" "] * 3
	for key, candids in possib_dict.items():
		build[0] = key
		candids_size = len(candids)

		for i in range(0, candids_size):
			build[1] = candids[i]
			for k in range(i+1, candids_size):
				build[2] = candids[k]
				phrase = ' '.join(build)
				phrase_length = len(phrase)
				if(phrase_length == ANAGRAM_LENGTH):
					if(exists_in_anam("".join(build))):
						list_of_l += combs(build, 3)

	# Check the combinations one by one to find the anagrams
	for candid in list_of_l:
		candid_hash = hashlib.md5(candid).hexdigest()
		if(candid_hash == HASH_EASY):
			print "THIS IS easy => "+candid
		elif(candid_hash == HASH_INTERMEDIATE):
			print "THIS IS intermediate => "+candid
		elif(candid_hash == HASH_HARD):
			print "THIS IS very hard => "+candid


if __name__ == "__main__":
    cProfile.run('main()')


