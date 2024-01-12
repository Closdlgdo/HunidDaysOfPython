# An Application Programming Interface (API) is a set of commands, functions, protocols and objects that programmers use to create
# software or interact with an external system.
# An API Endpoint is the website of the application. Like api.example.com.
# The API Request is when we are asking the website for information. We cant just take money from
# a bank safe, we need to make a request to the teller. That is an api request.
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    raise Exception("Error: " + response.status_code)
else:
    data = response.json()
    print(data)

# The type of response returns depend on the number returned. For example:
# 1xx -> Informational, 2xx -> Success, 3xx -> Redirection (you are not allowed in here),
# 4xx (you screwed up somewhere)-> Client Error, 5xx -> Server Error (the server messed up, not you)
