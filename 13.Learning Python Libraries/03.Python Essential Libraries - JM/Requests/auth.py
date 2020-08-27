# Python Essential Libraries by Joe Marini course example
# Example file for the Requests library
import requests
from requests.auth import HTTPDigestAuth

# define user and password values
user = "theuser"
passwd = "thepass"

# use the basic authentication method
url = "https://httpbin.org/basic-auth/theuser/thepass"
resp = requests.get(url, auth=(user,passwd))
print(resp.status_code)
print(resp.text)

# use the digest authentication method
url = "https://httpbin.org/digest-auth/auth/theuser/thepass"
resp = requests.get(url, auth=HTTPDigestAuth(user,passwd))
print(resp.status_code)
print(resp.text)