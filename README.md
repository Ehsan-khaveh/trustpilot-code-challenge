# Trustpilot Code Challenge
The solution for Trustpilot's "Follow the white rabbit" [code challenge](https://followthewhiterabbit.trustpilot.com/cs/step3.html).

## Solution Outlines:
1. Read in the words from the file and filter out the ones with letters not in anagram. 
2. Create a dictionary of filtered words mapped to to candidates with which they can build a phrase without violating letters in anagram.
3. Start building phrase of length 3 using the word_candidate map, and go higher until all the targets are found

## Requirements:
Python 2.7.12 

## Run the Code:
``` 
python solution.py
```








