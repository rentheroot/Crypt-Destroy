#Main File for Renee Schmidt's all purpose crypto and stego tool, Crypt-Destroy

#===imports===#
import enchant
from EnglishChecker import *
from Ciphers import *

#===Define Dictionaries===#
englishDict = enchant.Dict("en_US")

#===Define Variables===#

#input text to decrypt
uneditedText = "uryybjbeyqvzerarr"
#output text to find words in
editedText=  caesar_decrypt(uneditedText)
#minimum length required to count as a word
minWordLen = 4


#===Functions===#

#check if string has words in English
check_if_english(englishDict, editedText, minWordLen)