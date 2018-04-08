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
	letterDict = {'t': '19', 'z': '25', 'k': '10', 'y': '24', 'u': '20', 'f': '5', 'c': '2', 'p': '15', 'l': '11', 'v': '21', 'g': '6', 'x': '23', 'w': '22', 'b': '1', 'i': '8', 'o': '14', 'j': '9', 'h': '7', 'q': '16', 'd': '3', 'r': '17', 'm': '12', 'e': '4', 'a': '0', 'n': '13', 's': '18'}
	numberDict = {'15': 'p', '5': 'f', '19': 't', '25': 'z', '21': 'v', '11': 'l', '13': 'n', '12': 'm', '22': 'w', '10': 'k', '4': 'e', '8': 'i', '17': 'r', '1': 'b', '20': 'u', '7': 'h', '3': 'd', '24': 'y', '16': 'q', '0': 'a', '6': 'g', '14': 'o', '2': 'c', '18': 's', '23': 'x', '9': 'j'}
	#set text to string
	text = str(ue).lower()
	text = text.replace(' ', '')

	#make empty list for word
	decryptedWord = []

	decryptedText = []


	#for each letter in the alphabet
	for i in range(1,26):
		#for each number in text
		for number in text:

			number = letterDict[number]
			#set equation variables
			x = int(number)
			k = i

			#decrypt character by character
			decryptedCharacter = (x-k) % 26
			#lookup calculated number in dictionary
			decryptedCharacter = numberDict[str(decryptedCharacter)]

			decryptedWord.append(decryptedCharacter)
		
		decryptedWord = ''.join(decryptedWord)
		#append decrypted text
		decryptedText.append(decryptedWord)
		#reset decrypted word
		decryptedWord = []
				
		
	print(decryptedText)
	#return list of possible decryptions
	return(decryptedText)

