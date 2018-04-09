#Main File for Renee Schmidt's all purpose crypto and stego tool, Crypt-Destroy

#===imports===#
import enchant
from EnglishChecker import *
from Ciphers import *

#===Define Dictionaries===#
englishDict = enchant.Dict("en_US")
with open('allciphertext.txt','w') as the_file:
	pass
#===Define Variables===#

#input text to decrypt
uneditedText = "bmabmvkwlmlkimaizkqxpmz"
#output text to find words in
caesarResult = caesar_decrypt(uneditedText)
editedText = affine_decrypt(uneditedText,caesarResult)
#minimum length required to count as a word
minWordLen = 4


#===Functions===#

#check if string has words in English
try:
	check_if_english(englishDict, editedText, minWordLen)
except:
	print("Sorry, no valid English results returned")