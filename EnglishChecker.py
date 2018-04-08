#Determine if text is written in English

#===Imports===#
import enchant

#===Check if any word in string is English===#
#d is dictionary
#et is edited text
#wl is the minimum length of a word to count as english
def check_if_english(d,et,wl):
	

	#set stringHasText = false
	stringHasText = False
	
	#check for english words throughout entire string
	for ciphertext in et:
		
		#make edited text a string
		text = str(ciphertext)
		#set text length
		textLen = len(text)
		#set the word length to an integer
		wordLen = int(wl)


		while not stringHasText:
			for startingLetter in range(textLen):
				for endingLetter in range(wordLen + startingLetter, textLen + 1):
					if d.check(text[startingLetter:endingLetter]):
						stringHasText = True

			if stringHasText:
				print(text)			
		stringHasText = False

