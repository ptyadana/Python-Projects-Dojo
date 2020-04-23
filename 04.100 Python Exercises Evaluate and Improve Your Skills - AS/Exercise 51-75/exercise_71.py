# Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt

# Expected output: 

# 47

# Answer:
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
r = requests.get("http://www.pythonhow.com/data/universe.txt",headers={'User-Agent':user_agent})

content = r.text
a_letter_counts = content.count('a')
print(f'a_letter_counts : {a_letter_counts}')
