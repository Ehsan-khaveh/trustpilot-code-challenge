import hashlib
import cProfile
import itertools

############# DECLARATION OF CONSTANTS #############

ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_SORTED = ''.join(sorted(ANAGRAM)).strip()+"~"
ANAGRAM_LETTERS_LENGTH = len(ANAGRAM_SORTED)
# ANAGRAM_HASH = hashlib.md5(ANAGRAM).hexdigest()

HASH_EASY = "e4820b45d2277f3844eac66c903e84be"
#easy string = "printout stout yawls"
HASH_INTERMEDIATE = "23170acc097c24edb98fc5488ab033fe"
HASH_HARD = "23170acc097c24edb98fc5488ab033fe"

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

# def subfinder(parent, child):
# 	intersect = set(parent).intersection(set(child))
# 	return not set(parent).isdisjoint(child)

# words_list = [line.rstrip('\n') for line in open(LIST_FILE_NAME)]

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
			# elif(len_comb+1 == ANAGRAM_LENGTH):
			# 	k += 1
			j += 1

			# elif 
		if(len(comb_list) > 0):
			possib_dict[word] = comb_list

	# print k
	print len(possib_dict["stout"])


		
if __name__ == "__main__":
    cProfile.run('main()')


