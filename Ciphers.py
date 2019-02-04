#imports
import string
from fractions import gcd
#===replace letters with numbers===#
def letter_to_number(text, operation):
	#set letter to number dict
	letterDict = {'t': '19', 'z': '25', 'k': '10', 'y': '24', 'u': '20', 'f': '5', 'c': '2', 'p': '15', 'l': '11', 'v': '21', 'g': '6', 'x': '23', 'w': '22', 'b': '1', 'i': '8', 'o': '14', 'j': '9', 'h': '7', 'q': '16', 'd': '3', 'r': '17', 'm': '12', 'e': '4', 'a': '0', 'n': '13', 's': '18'}
	numberDict = {'15': 'p', '5': 'f', '19': 't', '25': 'z', '21': 'v', '11': 'l', '13': 'n', '12': 'm', '22': 'w', '10': 'k', '4': 'e', '8': 'i', '17': 'r', '1': 'b', '20': 'u', '7': 'h', '3': 'd', '24': 'y', '16': 'q', '0': 'a', '6': 'g', '14': 'o', '2': 'c', '18': 's', '23': 'x', '9': 'j'}

	#make empty list for word
	decryptedWord = []
	decryptedText = []

	#for each letter in the alphabet
	for i in range(0,26):
		#for each number in text
		for number in text:

			number = letterDict[number]
			#set equation variables
			x = int(number)
			k = i

			#decrypt character by character
			decryptedCharacter = eval(operation)
			
			#lookup calculated number in dictionary
			decryptedCharacter = numberDict[str(decryptedCharacter)]

			decryptedWord.append(decryptedCharacter)
		
		decryptedWord = ''.join(decryptedWord)
		#append decrypted text
		decryptedText.append(decryptedWord)
		#reset decrypted word
		decryptedWord = []
	
	#return list of possible decryptions
	return(decryptedText)



#===Caesar Cipher===#

#|Algorithm|#
#k = key (shift)
#x = character to decrypt
#e(x) = encryption function
# e(x)=(x-k) % 26

#ue = unedited text
def caesar_decrypt(ue):
	#set text to string
	text = str(ue).lower()
	text = text.replace(' ', '')
			
	decryptedText = letter_to_number(text, '(x-k) % 26')
	
	#return list of possible decryptions
	return(decryptedText)

#===atbash decryption===#
def atbash_decrypt(ue):

	#make alphabet lists
	correctAlpha = list(string.ascii_lowercase)
	reverseAlpha = list(string.ascii_lowercase)
	reverseAlpha.reverse()

	#map alphabet lists to a dictionary
	alphaDict = dict(zip(correctAlpha,reverseAlpha))

	text = str(ue).lower()
	text = text.replace(' ', '')

	decryptedText = []

	for character in text:
		if character in alphaDict:
			decryptedText.append(alphaDict[character])

	finalString = ''.join(decryptedText)
	print(finalString)
	return(finalString)

#===Affine cipher decryption===#
#|Algorithm|#
#D ( x ) = a^-1 ( x - b ) mod m
#a^-1 = modular multiplicative inverse of a modulo m
#ax = 1 mod m (multiplicative inverse)
def affine_decrypt(ue):
	uneditedText= ue.lower()

	#set letter to number dict
	letterDict = {'t': '19', 'z': '25', 'k': '10', 'y': '24', 'u': '20', 'f': '5', 'c': '2', 'p': '15', 'l': '11', 'v': '21', 'g': '6', 'x': '23', 'w': '22', 'b': '1', 'i': '8', 'o': '14', 'j': '9', 'h': '7', 'q': '16', 'd': '3', 'r': '17', 'm': '12', 'e': '4', 'a': '0', 'n': '13', 's': '18'}
	numberDict = {'15': 'p', '5': 'f', '19': 't', '25': 'z', '21': 'v', '11': 'l', '13': 'n', '12': 'm', '22': 'w', '10': 'k', '4': 'e', '8': 'i', '17': 'r', '1': 'b', '20': 'u', '7': 'h', '3': 'd', '24': 'y', '16': 'q', '0': 'a', '6': 'g', '14': 'o', '2': 'c', '18': 's', '23': 'x', '9': 'j'}
	modInversesList = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

	#turn into numbers
	numberText =[]
	for letter in uneditedText:
		newLetter= letterDict[letter]
		numberText.append(int(newLetter))

	decryptedText = []
	#for each value of b
	for b in range(1,27):
		
		
		for a in modInversesList:
			decryptedNumber = []
			for letNum in numberText:
				newNumber = (a * (letNum - b))%26
				
				newNumber2 = numberDict[str(newNumber)]
				decryptedNumber.append(newNumber2)
			#decrypted string
			
			decryptedNumber = ''.join(decryptedNumber)
			decryptedText.append(decryptedNumber)
	return(decryptedText)



	
