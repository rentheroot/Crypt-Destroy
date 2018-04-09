#===Imports===#
import string

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


