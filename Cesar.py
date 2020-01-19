alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
word = input("Write your word: ")
n = len(word)
key = 1
outword = ""
for i in range(n) :
	character = word[i]
	position = alph.find(character)
	newPosition = position + key
	outword += alph[newPosition]	
print("Your word siphred : ", outword)

				


