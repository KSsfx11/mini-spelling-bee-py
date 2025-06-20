# This program will spell out a word letter by letter and then print the word in full. 
# its like a mini spelling bee!
word = input("what word would you like me to spell?: ")
for letter in word:
    print(letter)
print(word)
input("Anything else? (press enter to exit)")