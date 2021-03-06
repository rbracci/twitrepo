# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%
##
# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

print("START*******")

import nltk 
import random
from nltk import word_tokenize, sent_tokenize
nltk.download('punkt')


debug = False 

if debug:
	print ("Getting information from file madlib_test.txt...\n")

firststring = (text2 [:150]) #finds the first 150 tokens
para = ' '.join(firststring)

tokens = nltk.word_tokenize(para)
print("TOKENS") 
print(tokens) #printing the tokens from the nltk text2 book 
taggedtokens = nltk.pos_tag(tokens) 
print("TAGGED TOKENS")
print(taggedtokens) #printing the tagged tokens
if debug:
	print ("First few tagged tokens are:")
	for tup in taggedtokens[:5]: #sets the limit of 5 tagged tokens that I am looking for
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","NNP":"Proper noun, singular","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.10,"NNP":.10,"VB":.10,"JJ":.10, "VPB":.10} #gives the possibilities of what it is looking for and the probability 

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in taggedtokens: #using a tuble to iterate through taggedtokens
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word)) #appending the final_words if it meets the requirements above
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag])) 
		final_words.append(spaced(new_word)) #appending new_word if it meets the requirement above

print ("".join(final_words))


print("\n\nEND*******")
