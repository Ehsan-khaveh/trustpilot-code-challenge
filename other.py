# -*- coding: utf-8 -*-
# md5 of our target: 4624d200580677270a54ccff86b9610e
# This code ran in 48.6 seconds on a 2.5Ghz i7 Macbook Pro OSX 10.10.5


# set recursive depth to limit the length of the word combo we check. 
# change this if a different depth is desired:
depth = 3


# import useful things
from datetime import datetime
startTime = datetime.now()
from collections import defaultdict, deque
import hashlib
import itertools
import sys


# load words
mySet = set(open('wordlist'))
mySet = set(map(lambda s: s.strip(), mySet))


# initialize check as our dictionary with letter counts to check against
check = defaultdict(int)
letterString = 'poouulttttrywissan'
for letter in letterString:
    check[letter] += 1


# strip out words from mySet that have the wrong letters
goodLetters = str('poultrywisan')
newset = set()
for word in mySet:
    for letter in word: 
        if letter not in goodLetters:
            newset.add(word)
            break
mySet.difference_update(newset)


# strip out words from mySet that have too many of the right letters
newset.clear()
for word in mySet:
    c = defaultdict(int)
    for letter in word:
        c[letter] += 1
    for letter in goodLetters:
        if c[letter] > check[letter]:
            newset.add(word)
            break
mySet.difference_update(newset)


# define list to iterate over, sort, and reorder to make search most efficient
newList = list(mySet)
newList.sort(lambda x,y: cmp(len(x), len(y)))
newList.reverse()


# put the likely words containing between 4 and 7 letters up front so we check combos of them first
countLow = 0
countHigh = 0
for word in newList:
    if len(word) > 3:
        countLow += 1
    if len(word) > 7:
        countHigh += 1
newList = newList[countHigh : countLow] + newList[: countHigh] + newList[countLow :]


# main recursive function.
def recurseHash(combo, counts):
    for elem in newList:
        if elem in combo:
            continue
        else:
            # update counts
            for letter in elem:
                counts[letter] += 1

            # set flags to tell if our combo has not enough, or too many, of any letter
            lessFlag = 0
            greaterFlag = 0
            for letter in check:
                if counts[letter] < check[letter]:
                    lessFlag = 1
                elif counts[letter] > check[letter]:
                    greaterFlag = 1

            # check flags and either hash combo, call recurseHash again, or do nothing
            if greaterFlag == 0:
                combo.append(elem)
                if lessFlag == 0:
                    if hashlib.md5(" ".join(combo)).hexdigest() == '4624d200580677270a54ccff86b9610e':
                        print "Success: ", " ".join(combo)
                        print datetime.now() - startTime
                        sys.exit(0)
                elif len(combo) < depth:
                    recurseHash(combo, counts)
                combo.remove(elem)

            # remove letters from counts
            for letter in elem:
                counts[letter] -= 1

recurseHash(deque(), defaultdict(int))