#Determine if text is written in English

#===Imports===#
import enchant
import threading

#===multithreading===#
def check_word(ct,wl,d):
	#make edited text a string
	ciphertext = ct
	text = str(ciphertext)
	#set text length
	textLen = len(text)
	#set the word length to an integer
	wordLen = int(wl)
	#set stringHasText = false
	stringHasText = False

	while not stringHasText:
		for startingLetter in range(textLen):
			for endingLetter in range(wordLen + startingLetter, textLen + 1):
				if d.check(text[startingLetter:endingLetter]):
					stringHasText = True

		if stringHasText:
			print(text)
			with open('allciphertext.txt','a') as the_file:
				the_file.write(text + '\n')

		else:
			break

#===Check if any word in string is English===#
#d is dictionary
#et is edited text
#wl is the minimum length of a word to count as english
def check_if_english(d,et,wl):
	


	threads = []
	
	#check for english words throughout entire string
	for ciphertext in et:

		ct = ciphertext
		t = threading.Thread( target= check_word, args=(ct, wl,d))
		threads.append(t)
		t.start()
		t.join()
			
		#t.start()

		#stringHasText = False

