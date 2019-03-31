# This function takes a pdf and converts it to a binary file 
def readfilePDF():
	file = open('bin.txt', 'wb')
	for line in open('example.pdf', 'rb').readlines():
		file.write(line)
	file.close()

# This function takes the file bin.txt which was converted from a pdf, and
# converts it back into the same pdf
def writefilePDF(pdfFile, binaryFile):
	file = open(pdfFile, 'wb')
	for line in open(binaryFile, 'rb').readlines():
		file.write(line)
	file.close()

# This function takes a text file called original.txt and converts it to 
# a binary file, binary.txt
def readFileTXT():
	file = open('binary.txt', 'wb')
	for line in open('original.txt', 'rb').readlines():
		file.write(line)
	file.close()

# This function takes a binary file, binary.txt, and converts it back to a
# readable text file
def writeFileTXT():
	file = open('output.txt', 'wb')
	for line in open('binary.txt', 'rb').readlines():
		file.write(line)
	file.close()


def toBinary():
	# This will be the binary file from the pdf, with each character separated by spaces
	# Put it in file first to save it
	file = open('newfile.txt', 'wb') 
	with open("code.txt", "r", encoding = "ISO-8859-1") as File1:
		St = (' '.join(format(ord(x), 'b') for x in File1.read()))
		file.write(St.encode())
	file.close()
	
	line = []
	# Read binary file back in, everyting is stored on in line, so loop
	# only executes once
	for line in open('newfile.txt', 'rb').readlines():
		continue
	
	# open the file to store the properly formatted binary
	file = open('binaryToEncode.txt', 'w')
	
	line = str(line)
	binNum = []
	first = True
	for i in range(0, len(line)):
		
		if line[i] == ' ':  # At the end of each binary number
			if first == True:
				binNum = binNum[2:]
				first = False
			temp = str(''.join(map(str, binNum))) # convert string to int
			#print("binary   " + str(temp.zfill(8)))
			data = int(str(temp), 2)  # convert binary to decimal number
			del binNum[:]			  # delete to retrieve the next number
			#print("decimal   " + str(data))
			file.write(str(temp.zfill(8)))  # write the binary number to the file, all 8 bits, padded with 0's
			file.write(" ")
		else:
			binNum.append(line[i])
	file.close()
	
	# Will result in a file called binaryToEncode.txt that has 8 bit numbers that
	# represent all of the characters in the binary file that was converted from the pdf
	# ***Use this function and the file that is created in this function to do the el gamal scheme
##########################################################################################
# This function doesn't work all the way yet. It is supposed to take the binary file
# that we converted in the toBinary function, convert it back to the original characters for the pdf
# and then that file will be opened as a pdf
# But I think there's something wrong with the encoding. It puts the correct characters in the ASCIItoPDF.txt
# file but the unknown symbols are different
def fromBinaryToASCII():
	for line in open('binaryToEncode.txt', 'r').readlines():
		continue
		
	file = open('ASCIItoPDF.txt', 'w', encoding="utf-16")
	line = str(line)
	binNum = []
	
	for i in range(0, len(line)):
		if line[i] == ' ':
			temp = str(''.join(map(str, binNum)))
			data = int(str(temp), 2)
			#print(chr(data))
			del binNum[:]
			file.write(chr(data))
		else:
			binNum.append(line[i])
	file.close()
		
def main():

	readfilePDF()
	toBinary()
	fromBinaryToASCII()
	writefilePDF("out.pdf", "ASCIItoPDF.txt")
	
if __name__ == "__main__":
	main()
