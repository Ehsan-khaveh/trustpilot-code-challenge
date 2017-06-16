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

LIST_FILE_NAME = "wordlist"

L = 0

################# HELPER FUNCTIONS #################

def exists_in_anam(child):

	child = sorted(child)

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

def is_anagram(phrase, phrase_length):
	if(phrase_length <= ANAGRAM_LENGTH):
		if(exists_in_anam("".join(phrase))):
			return True
def combs(n, r):
	return [" ".join(map(str, comb)) for comb in permutations(n, r)]
	

# def nest(word, built, index, L):
# 	if(L = 1):
# 		return built
# 	for 

def recur(dic, key, listed, d):
	if (d == 1):
		dic[key] = listed
		return
	for key, value in dic.iteritems():
		dict((w,[]) for w in listed)
		dic[val]
		del newDic[key]
		newDic[key] = recur(newDic, d-1)


def main():

	words_set = set()

	# store the word list in a set 
	# in this way we get rid of duplicates too
	for line in open(LIST_FILE_NAME):
		word = line.rstrip('\n')
		# filter out words that have letters which are not in the anagram
		if (word.isalnum() and exists_in_anam(word)):
			words_set.add(word)

	# things we need for inside
	word_list = list(words_set)
	phrase = [""] * 3
	phrase_length = [0] * 3
	filtered_len = len(word_list)
	len_dict = {}
	for word in word_list:
		len_dict[word] = len(word)

	counter = 0

	for ind, val in enumerate(word_list):
		# print "ind = "+str(ind)
		j = ind
		phrase[0] = val
		phrase_length[0] = len_dict[val]
		while j < filtered_len:
			
			word1 = word_list[j]
			phrase[1] = word1
			phrase_length[1] = phrase_length[0]+len_dict[word1]

			if(is_anagram(phrase, phrase_length[1])):
				counter+=1
				# i = j
				# while i < filtered_len:
				# 	word2 = word_list[i]
				# 	phrase[2] = word2
				# 	phrase_length[2] = phrase_length[1]+len_dict[word2]+1
				# 	if(is_anagram(phrase, phrase_length[2])):
				# 		print phrase
				# 		counter += 1
				# 	i += 1
				# phrase[2] = ""
			j += 1

	print counter
	# recur(words_dict, 3)
	# word_list.sort(key=len, reverse=True)

	

	

	# # get all possible combination candidates for every word in the filtered list
	# for ind, word in enumerate(word_list):
	# 	comb_list = {}
	# 	j = ind
	# 	while j < filtered_len:
	# 		candid = word_list[j]
	# 		comb_list[candid] = []
	# 		while i < filtered_len
	# 			comb = word+candid
	# 			len_comb = len(comb)
	# 			i += 1
	# 		comb = word+candid
	# 		len_comb = len(comb)
	# 		# plus 1 to account for space
	# 		if(len_comb+1 <= ANAGRAM_LENGTH):
	# 			if(exists_in_anam(comb)):
	# 				comb_list.append(candid)
	# 		# elif(len_comb+1 == ANAGRAM_LENGTH):
	# 		# 	k += 1
	# 		j += 1

	# 		# elif 
	# 	if(len(comb_list) > 0):
	# 		possib_dict[word] = comb_list

	# # print possib_dict["stout"]

	# # combs = combinations(possib_dict["stout"], 3)

	# len_dict = {}
	# for word in word_list:
	# 	len_dict[word] = len(word)

	# r = 4

	# counter = 0

	# list_of_l = []
	# phrase = [""] * r
	# for key, candids in possib_dict.items():
	# 	n = len(candids)
	# 	if(r > n):
	# 		continue
	# 	indices = range(r-1)
	# 	phrase[0] = key
	# 	c = r-1
	# 	c_range = list(reversed(range(c)))
	# 	while(True):

	# 		# check if we have looked at all the combinations
	# 		for i in c_range:
	# 			if indices[i] != i + n - c:
	# 				break
	# 		else:
	# 			break


	# 		# Update the indices
	# 		indices[i] += 1
	# 		j = i+1
	# 		while (j<c):
	# 			indices[j] = indices[j-1] + 1
	# 			j += 1

	# 		# Fill up the phrase array based on updated indices
	# 		for k, i in enumerate(indices):
	# 			phrase[k+1] = candids[i]

	# 		# get phrase length
	# 		phrase_length = c
	# 		for word in phrase:
	# 			phrase_length += len_dict[word]
	# 		# phrase_length = sum(len_dict[word] for word in phrase) + c

	# 		# phrase_length = len_dict[phrase[0]] + len_dict[phrase[1]] + len_dict[phrase[2]] + 2
	# 		# c_diff = ANAGRAM_LENGTH+(c-2)

	# 		if(phrase_length == ANAGRAM_LENGTH+(c-2)):
	# 			if(exists_in_anam("".join(phrase))):
	# 				# print phrase
	# 				combo = combs(phrase, r)
	# 				for co in combo:
	# 					candid_hash = hashlib.md5(co).hexdigest()
	# 					if(candid_hash == HASH_EASY):
	# 						print "THIS IS easy => "+co
	# 					elif(candid_hash == HASH_INTERMEDIATE):
	# 						print "THIS IS intermediate => "+co
	# 					elif(candid_hash == HASH_HARD):
	# 						print "THIS IS very hard => "+co
	# 						sys.exit()
	# 		# elif(phrase_length > c_diff):
	# 		# 	indices[c-1] = n-1

	# 	counter += 1
	# 	print counter

if __name__ == "__main__":
    cProfile.run('main()')


