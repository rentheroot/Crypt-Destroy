#Main File for Renee Schmidt's all purpose crypto and stego tool, Crypt-Destroy

#===imports===#
import enchant
from EnglishChecker import *
from Ciphers import *
import string

#===Define Dictionaries===#
englishDict = enchant.Dict("en_US")

with open('allcipherText.txt', 'w') as the_file:
	pass

#===Functions===#
def print_results(englishDict, editedText, minWordLen):
	#check if string has words in English
	try:
		check_if_english(englishDict, editedText, minWordLen)
	except:
		print("Sorry, no valid English results returned")

#===Define Variables===#
with open('encryptedText.txt', 'r') as the_file:\
	#minimum length required to count as a word
	minWordLen = 4
	#input text to decrypt
	uneditedText = the_file.readlines()
	for i in uneditedText:
		i = i.lower()
		i = i.replace(' ','')
		#output text to find words in
		editedText = affine_decrypt(i)
		print_results(englishDict, editedText, minWordLen)
		editedText = caesar_decrypt(i)
		print_results(englishDict, editedText, minWordLen)
		editedText = atbash_decrypt(i)
		print_results(englishDict, editedText, minWordLen)


