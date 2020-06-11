"""Reterive and print words from a URL.

Usage:

    python3 words.py <URL>
    Example: python words.py http://sixty-north.com/c/t.txt
"""

import requests
import sys


def fetch_words(url):
    """Fetch a list of string from URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing words from the document.
    """
    user_agents = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    headers = {'User-Agents':user_agents}

    response = requests.get(url,headers = headers)

    story_word = []
    for line in response.text.split('\n'):
        line_word = line.split()
        for word in line_word:
            story_word.append(word)
    return story_word


def print_words(story_word):
    """Print items one per line.

    Args:
        An iterable series of printable items. 
    """
    for word in story_word:
        print(word)


def main(url):
    """Print each word from a text document from at a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_words(words)


if __name__ == "__main__":
    url = sys.argv[1] # The 0th arg is the module filename.
    main(url)