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
HASH_HARD = "665e5bcb0c20062fe8abaaf4628bb154"

LIST_FILE_NAME = "wordlist"

################# HELPER FUNCTIONS #################

def isalphanum(string):
	return string.isalnum()

def quick_sort(string):
	return ''.join(sorted(string))

def is_substring(string, string_len):

	if(ANAGRAM_LENGTH < string_len):
		return False

	# by sorting we save some time here, we avoid a nested loop
	i = 0
	for letter in string:

		while i != ANAGRAM_LENGTH:
			letter_m = ANAGRAM_SORTED[i]
				
			if(letter_m > letter):
				return False

			i += 1
			if(letter_m == letter):
				break

	return True


# words_list = [line.rstrip('\n') for line in open(LIST_FILE_NAME)]

def main():

	words_dict = {}
	# words_set = set()

	# store the word list in a dictionary 
	# in this way we get rid of duplicates too
	for line in open(LIST_FILE_NAME):
		word = line.rstrip('\n')
		word_sorted = quick_sort(word)

		# filter out words that have letters which are not in the anagram
		if (isalphanum(word)):
			word_length = len(word)
			if(is_substring(word_sorted, word_length)):
				words_dict[word] = word_length


	word_list = list(words_dict.items())
	word_list.sort(key=lambda tup: tup[1], reverse=True)

	# print len(word_tuple_list)

	for word1 in word_list:
		for word2 in word_list:
			for word3 in word_list:
				concat = word1[0]+" "+word2[0]+" "+word3[0]
				concat_length = word1[1]+word2[1]+word3[1]+2
				if(concat_length == ANAGRAM_LENGTH):
					if(ANAGRAM_SORTED == quick_sort(concat)):
						candid_hash = hashlib.md5(concat).hexdigest()
						if(candid_hash == HASH_EASY):
							print "THIS IS easy => "+concat
						elif(candid_hash == HASH_INTERMEDIATE):
							print "THIS IS intermediate => "+concat
						elif(candid_hash == HASH_HARD):
							print "THIS IS very hard => "+concat
	    


		
if __name__ == "__main__":
    cProfile.run('main()')


