# Application Programming Interface. Third party services that we can write code to talk to.
# We basically pretend to be a browser, connect to the api on a server and download some data that we can add to our page.
# A popular package that pip has is called requests. The request library allows us to make HTTP/s requests.
# JSON is a language agnostic format that is used to transfer data from one program to another.
import sys

import requests

if len(sys.argv) != 2:  # error checking; if len(sys.argv) is not equal to 2. we exit and print something.
    sys.exit("Too many arguments!")
# request.get is a function inside the request package that allows us to make HTTP/s requests.
# it gets stored in a variable called response.
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())
