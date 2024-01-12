# An Application Programming Interface (API) is a set of commands, functions, protocols and objects that programmers use to create
# software or interact with an external system.
# An API Endpoint is the website of the application. Like api.example.com.
# The API Request is when we are asking the website for information. We cant just take money from
# a bank safe, we need to make a request to the teller. That is an api request.
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
