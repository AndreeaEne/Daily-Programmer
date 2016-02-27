# We have discovered a new species of aliens! They look like this [1] and are trying to communicate with us using the /r/ggggg[2] subreddit! As you might have been able to tell, though, it is awfully hard to understand what they're saying since their super-advanced alphabet only makes use of two letters: "g" and "G". Fortunately, their numbers, spacing and punctuation are the same.
# We are going to write a program to translate to and from our alphabet to theirs, so we can be enlightened by their intelligence.
# Feel free to code either the encoding program, the decoding program, or both.
# Also, please do not actually harass the residents of /r/ggggg[3] .

from sys import argv


# Decoding for keys of fixed length 3
# def decode(t):
# 	decoded_text = ''
# 	for word in t.split(" "):
# 		if len(word) > 3 :
# 			for i in range(0, len(word) - 3, 3):
# 				newWord = word[i:i+3]
# 				# print (i, newWord, key_dictionary[newWord])
# 				if newWord.isalpha() and newWord in key_dictionary:
# 					decoded_text += key_dictionary[newWord]
# 			if len(word) % 3 == 1:
# 				decoded_text += word[i+3] + ' '
# 	print(decoded_text)

def decode(substitutions, text):
	# The input comes as letter followed by a group of letters representing its substitution
	# so we make a dictionary out of them
	keys = substitutions.split()
	dictionary = dict(zip(keys[1::2], keys[::2]))

	start = 0
	decoded = ''
	for stop in range(len(text) + 1):
		# Check until we find a substitution in the dict
		if text[start:stop] in dictionary:
			decoded += dictionary[text[start:stop]]
			start = stop
		# White space and punctuation is copied as is
		elif text[start] not in {'g', 'G'}:
			decoded += text[start]
			start = stop
	return decoded


substitutions = argv[1]
text = argv[2]
print (decode(substitutions, text))
