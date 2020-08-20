#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("test.txt"):
    # get the path to the file in the current directory
    src = path.realpath("test.txt")
    
    # let's make a backup copy by appending "bak" to the name
    duplicate = src + ".bak"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(src, duplicate) # copy only the file
    shutil.copystat(src, duplicate) # aslo copy the meta data such as modification time, etc

    # rename the original file
    os.rename("test2.txt", "newtest.txt")
    
    # now put things into a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("testarchive", "zip", root_dir=root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write("test.txt")
      newzip.write("test.txt.bak")


      
if __name__ == "__main__":
  main()
