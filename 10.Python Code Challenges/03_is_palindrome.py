"""
Palindrome: word or phrase that reads the same forwards as backwards
Input: string of word or phrase
Output: True/False
Only consider letters (A-Z)
Ignore Capital Letters
Example: level => Palindrome
Example: Racecar => Palindrome
Example: Go hang a salami - I'm a lasagna hog => Palindrome
"""

import re

def is_palindrome(st):
    forwards = "".join(re.findall("[A-Za-z]+", st.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


if __name__ == "__main__":
    st = input("Enter a string: ")
    result = is_palindrome(st)
    print("It is a Palindrome." if result else "It is NOT a Palindrome.")