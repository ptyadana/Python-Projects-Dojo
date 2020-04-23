# Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . 
# Make sure the file has that name exactly.

# Then just paste the following code in the file:

# import requests

# r = requests.get("http://www.pythonhow.com")
# print(r.text[:100])

# Executing the script will throw an error. 
# Please fix something to make the program print out the expected output. 
# You should not modify the code itself, but something else.

# Expected output: 

# <!DOCTYPE html>
# <!--[if IE 7]>
# <html class="ie ie7" lang="en-US" prefix="og: http://ogp.me/ns#">


#Answer:
import requests
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
r = requests.get("http://www.pythonhow.com",headers={'User-Agent':user_agent})
print(r.status_code)
print(r.text[:100])

# Answer: 
# Rename the file name from requests.py  to something else.

# Explanation:
# In the code Python is actually referring to the script name which is requests  and it doesn't find a get attribute for that name. Script names load in the current namespace. They are actually stored in the __name__  variable. You could try to print that variable out and you would see that it prints your script name. Therefore you should not name your scripts under library names. 
