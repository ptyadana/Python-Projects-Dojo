# Python Essential Libraries by Joe Marini course example
# Example file for using Requests library
import requests

# use a timeout value for a request
resp = requests.get("https://httpbin.org/delay/0.5", timeout=1.0)
print(resp.status_code)

# simulating timeout error => website took 2.0 seconds to response, our program only wait for 1.0 seconds otherwise throw timeout error
resp = requests.get("https://httpbin.org/delay/2.0", timeout=1.0)
print(resp.status_code)


# introspect the redirection history
resp = requests.get("http://github.com")      # github redirects http request to more secure https
print(resp.url)
print(resp.history)
print()
original = resp.history.pop()
print(original.url)
print(original.status_code)
print(original.reason)

# Use a session object to group requests and settings
sess = requests.Session()
sess.get("https://httpbin.org/cookies/set/sample/123456789")
resp = sess.get("https://httpbin.org/cookies")
print(resp.text)

# Customize the user-agent to simulate different browsers
# Set the user-agent to be Firefox
sess.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"
})
resp = sess.get("http://google.com")
print(len(resp.content))

# Set the user-agent to be an iPhone
sess.headers.update({
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) relesys_web_client/1.3.10.0 (RelesysApp/1.3.43 net.relesysapp.nettoenterprise)"
})
resp = sess.get("http://google.com")
print(len(resp.content))