#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("test.txt", "w+")

  # Open the file for appending text to the end
  # f = open("test.txt", "a")
  f = open("test.txt", "r")

  # write some lines of data to the file
  # for i in range(10):
  #   f.write(f"This is line {i} \n")
  
  # close the file when done
  # f.close()
  
  # Open the file back up and read the contents
  if f.mode == "r":
    # contents = f.read()
    # print(contents)

    fl = f.readlines()
    for content in fl:
      print(content)
    
if __name__ == "__main__":
  main()
