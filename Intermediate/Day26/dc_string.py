# we will use dictionary comprehension to create a dictionary called result that takes each word in the given sentence
# and calculates the number of letters in each word.
sentence = input("Please enter a sentence: ")

result = {word: len(word) for word in sentence.split()}

print(result)
