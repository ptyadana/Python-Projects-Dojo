# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser


meta_count = 0;

class MyHTMLParser(HTMLParser):
  
  def handle_comment(self, data):
    print("found comment : ", data)
    position = self.getpos()
    print("At Line: ", position[0], " , Position: ", position[1])
  
  def handle_starttag(self, tag, attrs):
    global meta_count

    if tag == "meta":
      meta_count += 1

    print("found start tag : ", tag)
    position = self.getpos()
    print("At Line: ", position[0], " , Position: ", position[1])

    if attrs.__len__() > 0:
      print("Attributes")
      for a in attrs:
        print(a[0], " = ",  a[1])

  def handle_endtag(self, tag):
    print("found end tag : ", tag)
    position = self.getpos()
    print("At Line: ", position[0], " , Position: ", position[1])

  def handle_data(self, data):
    if data.isspace():
      return
    position = self.getpos()
    print("found data: ", data)
    print("At Line: ", position[0], ", Position: ", position[1])

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()

  with open("samplehtml.html", "r") as f:
    contents = f.read()
    parser.feed(contents)

if __name__ == "__main__":
  main();
  