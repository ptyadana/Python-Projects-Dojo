# HTML Parser Module
from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for att in attrs:
            print("Attrs: ", att)
    
    def handle_endtag(self, tag):
        print("End tag: ", tag)
        
    def handle_comment(self, data):
        print("Comment: ", data)
        
    def handle_data(self, data):
        print("Data: ", data)
        

# custom parser
parser = HTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>")
print()

# process user input hmtl
user_input = input("Put in HTML code to process: ")
parser.feed(user_input)
print()

# read html file
with open("data/test.html", "r") as file:
    content = file.read()
    parser.feed(content)

