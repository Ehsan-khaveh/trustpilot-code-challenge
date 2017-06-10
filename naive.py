import hashlib
import cProfile
import itertools

############# DECLARATION OF CONSTANTS #############

ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_SORTED = ''.join(sorted(ANAGRAM))
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

def is_substring(mother, child):

	if(len(mother) < len(child)):
		return False

	# by sorting we save some time here, we avoid a nested loop
	i = 0
	for letter in child:

		while i != len(mother):
			letter_m = mother[i]
				
			if(letter_m > letter):
				return False

			i += 1
			if(letter_m == letter):
				break

	return True


# words_list = [line.rstrip('\n') for line in open(LIST_FILE_NAME)]

def main():

	# words_dict = {}
	words_set = set()

	# store the word list in a dictionary 
	# in this way we get rid of duplicates too
	for line in open(LIST_FILE_NAME):
		word = line.rstrip('\n')
		word_sorted = quick_sort(word).strip()

		# filter out words that have letters which are not in the anagram
		if (isalphanum(word) and is_substring(ANAGRAM_SORTED.strip(), word_sorted)):
			words_set.add(word)
			# words_dict[word] = word_sorted

	
		# words_list = quick_sort(word)

	word_list = list(words_set)

	word_list.sort(key=len, reverse=True)

	for word1 in word_list:
		for word2 in word_list:
			for word3 in word_list:
				concat = word1+" "+word2+" "+word3
				if(len(concat) == ANAGRAM_LENGTH):
					if(ANAGRAM_SORTED == quick_sort(concat)):
						candid_hash = hashlib.md5(concat).hexdigest()
						if(candid_hash == HASH_EASY):
							print "THIS IS easy => "+concat
						elif(candid_hash == HASH_INTERMEDIATE):
							print "THIS IS hard => "+concat
						elif(candid_hash == HASH_HARD):
							print "THIS IS very hard => "+concat
	    


		
if __name__ == "__main__":
    cProfile.run('main()')


