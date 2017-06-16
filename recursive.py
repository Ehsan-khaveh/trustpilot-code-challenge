import hashlib
import cProfile
import itertools
from itertools import permutations

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

LIST_FILE_NAME = "wordlist"

L = 0

################# HELPER FUNCTIONS #################

# def quick_sort(string):
# 	if not string: 
# 		return ""
# 	else:
# 		pivot = string[0]
# 		lesser = quick_sort([x for x in string[1:] if x < pivot])
# 		greater = quick_sort([x for x in string[1:] if x >= pivot])
# 		return lesser + pivot + greater

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

# def subfinder(parent, child):
# 	intersect = set(parent).intersection(set(child))
# 	return not set(parent).isdisjoint(child)

# words_list = [line.rstrip('\n') for line in open(LIST_FILE_NAME)]

def recursion(words, length, build, pos, index):
	# print str(pos) + "  " +str(length)
	if (pos == length):
		phrase = " ".join(build)
		if(len(phrase) == ANAGRAM_LENGTH):
			if(exists_in_anam("".join(build))):
				candid_hash = hashlib.md5(phrase).hexdigest()
				if(candid_hash == HASH_EASY):
					print "THIS IS easy => "+candid
				elif(candid_hash == HASH_INTERMEDIATE):
					print "THIS IS intermediate => "+candid
				elif(candid_hash == HASH_HARD):
					print "THIS IS very hard => "+candid
				

		return

	for word in words[index:]:
		build[pos] = word
		recursion(words, length, build, pos+1, index+1)

# def combos(word_bag, length):
# 	init = [" "] * length
# 	recursion(word_bag, length, init, 0, 0)


def combinations(iterable, r):
	i = 0
	print "sth"
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
	    return
	indices = range(r-1)
	# print tuple(pool[i] for i in indices)
	while True:
	    for i in reversed(range(r)):
	        if indices[i] != i + n - r:
	            break
	    else:
	        return
	    indices[i] += 1
	    for j in range(i+1, r):
	        indices[j] = indices[j-1] + 1
	    # print list(pool[i] for i in indices)
	    i += 1
	    print i


def combs(n, r):
	return [" ".join(map(str, comb)) for comb in permutations(n, r)]
	
def main():

	words_set = set()

	# store the word list in a set 
	# in this way we get rid of duplicates too
	for line in open(LIST_FILE_NAME):
		word = line.rstrip('\n')
		# filter out words that have letters which are not in the anagram
		if (word.isalnum() and exists_in_anam(word)):
			words_set.add(word)

	# store some constant for reusability
	word_list = list(words_set)
	filtered_len = len(word_list)
	possib_dict = {}

	# sort the bag of words by length to make the later searhc more efficient
	# word_list.sort(key=len)

	# print word_list
	# print len(word_list)
	# print word_list[:600]

	# n = choose(word_list[:500],  3)

	# print n

	# print "L is "+str(L) 

	# print len(word_list)

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

	# print possib_dict["stout"]

	# combs = combinations(possib_dict["stout"], 3)

	print len(possib_dict)
	len_dict = {}
	for word in word_list:
		len_dict[word] = len(word)
	print len(len_dict)

	r = 3

	list_of_l = []
	build = [" "] * r
	
	for key, candids in possib_dict.items():
		n = len(candids)
		candids.sort(key=len)
		if(r > n):
			continue
		# indices = range(r-1)
		# build[0] = key
		# c = r-1

		init = [""] * r
		init[0] = key

		recursion(candids, r, init, 1, 0)

		# while(True):
			# for i in reversed(range(c)):
			# 	if indices[i] != i + n - c:
			# 		break
			# else:
			# 	break

			# indices[i] += 1
			# for j in range(i+1, c):
			# 	indices[j] = indices[j-1] + 1

			# for k, i in enumerate(indices):
			# 	build[k+1] = candids[i]

			# # print build
			# phrase_length = len_dict[build[0]] + len_dict[build[1]] + len_dict[build[2]] + 2
			# if(phrase_length == ANAGRAM_LENGTH+1):
			# 	if(exists_in_anam("".join(build))):
			# 		print build
			# 		list_of_l += combs(build, r)

	
	# print len(list_of_l)
		# candids_size = len(candids)

		# for i in range(0, candids_size):
		# 	build[1] = candids[i]
		# 	for k in range(i+1, candids_size):
		# 		build[2] = candids[k]
		# 		phrase_length = len_dict[build[0]] + len_dict[build[1]] + len_dict[build[2]] + 2
		# 		if(phrase_length == ANAGRAM_LENGTH):
		# 			if(exists_in_anam("".join(build))):
		# 				list_of_l += combs(build, 3)

	# print len(list_of_l)
	
	# for candid in list_of_l:
	# 	candid_hash = hashlib.md5(candid).hexdigest()
	# 	if(candid_hash == HASH_EASY):
	# 		print "THIS IS easy => "+candid
	# 	elif(candid_hash == HASH_INTERMEDIATE):
	# 		print "THIS IS intermediate => "+candid
	# 	elif(candid_hash == HASH_HARD):
	# 		print "THIS IS very hard => "+candid


	


		
if __name__ == "__main__":
    cProfile.run('main()')


