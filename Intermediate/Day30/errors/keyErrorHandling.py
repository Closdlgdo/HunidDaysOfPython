# eval() function will create a list of dictionaries using the given string.
facebook_posts = eval(input())

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError as error_message:
        print(f"The key {error_message} not exist.")
        continue

print(total_likes)
