# Print is my friend when I want to debug.

pages = 0
word_per_page = 0

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
# total_words = pages + word_per_page
total_words = pages * word_per_page
print(f"your total words are: {total_words}")  # This prints out the number of pages: total_words)

# When I print the code above, it doesn't do the math correctly. It only prints out the number of pages:
# Number of pages: 55
# Number of words per page: 634
# 55

# We fix line 7 where it had two equal signs which was not allowing for the computation to occur. Now there
# is a proper return of a value, however, the return itself seems off based on the math I do in my head.
# If I have 12 words in one page = that equals to 12 words total. However, if I add pages to that one Page and each page
# has 12 words each, then clearly the total would depend on the amount of pages we have.
# So the way we can calculate is to multiply the number of pages by the number of words per page, not use addition.
