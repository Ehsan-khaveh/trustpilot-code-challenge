ANAGRAM = "poultry outwits ants"
ANAGRAM_LENGTH = len(ANAGRAM)
ANAGRAM_SORTED = ''.join(sorted(ANAGRAM)).strip()
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