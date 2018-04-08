#imports

#===Caesar Cipher===#

#|Algorithm|#
#k = key (shift)
#x = character to decrypt
#e(x) = encryption function
# e(x)=(x-k) % 26

#ue = unedited text
def caesar_decrypt(ue):
	#set letter to number dict
	letterDict = {'m': 12, 'j': 9, 'o': 14, 'c': 2, 'g': 6, 'd': 3, 'e': 4, 'n': 13, 's': 18, 'f': 5, 'h': 7, 'y': 24, 'k': 10, 'l': 11, 'u': 20, 'q': 16, 'i': 8, 'p': 15, 'z': 25, 'x': 23, 'w': 22, 'a': 0, 'v': 21, 't': 19, 'r': 17, 'b': 1}
	#set text to string
	text = str(ue).lower()
	text = text.replace(' ', '')
	#make empty list for each shift
	allPossibleDecrypt = []
	#make empty list for word
	decryptedWord = []

	#convert text to numbers
	for letter in text:
		if letter in letterDict:
			letterString = str(letterDict[letter])
			text = text.replace(letter, letterString)
	print(text)

	#make shifts
	for number in text:
		for i in range(0,26):

			#set equation variables
			x = int(number)
			k = i

			#decrypt character by character
			decryptedCharacter = (x-k) % 26
			decryptedWord.append(decryptedCharacter)

			#add decrypted text to list
			allPossibleDecrypt.append(decryptedText)

			#reset decrypted word
			decryptedWord = []

	#return list of possible decryptions		
	return(allPossibleDecrypt)
