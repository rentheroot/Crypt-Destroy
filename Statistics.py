#===Imports===#
import string
import collections
#===Index of Coincidence===#
#the index of coincidence of an English plaintext message is usually between 1.50 and 2.00
#if the message consists of 50 or more letters. The larger the message,
#the closer it should be to 1.73.

def index_coincidence(inFile):
	
	with open (inFile, 'r') as the_file:
		
		for line in the_file:

			counts = []
			counts2 = []
			startNumber = 0
			textLength = len(line)

			#count up frequency of each letter in the line
			for letter in string.ascii_lowercase:
				counted = line.count(letter)
				counts.append(counted)

			#calculate f * (f -1)
			for number in counts:
				f = number
				newf = f * (f -1 )
				counts2.append(newf)

			#add up all the numbers in the list
			for number in counts2:
				startNumber += number



			#calculate N * (N-1)
			N = textLength
			newN = N * (N -1)

			#calculate f/n
			ic = startNumber/ newN

			print(ic)


def english_frequency(ue):
	englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
