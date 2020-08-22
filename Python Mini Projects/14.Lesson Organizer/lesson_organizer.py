"""
Automatically search the folder and copied the specific files into target folder.
Note: The program is written for my own specific needs.

Input: filepath, keyword to contain in the file
ouput: delete uncessary files other than files with keyword and move the folder to the highest level
"""

import glob
from pathlib import Path
import os
import shutil


def lesson_organizer(file_path, file_type, file_keyword, dir_keyword, destination_dir):
    
    if os.path.exists(file_path):

        paths = Path(file_path).glob("**/*" + file_type)

        for path in paths:
            path_in_str = str(path)
            print(path_in_str)

            if path_in_str.find(file_keyword) != -1:
                #get the chapter number name
                chapter_pos = path_in_str.index(dir_keyword)
                chapter = path_in_str[chapter_pos: chapter_pos + len(dir_keyword) + 2]
                print(chapter)

                lesson_name = path_in_str[path_in_str.rindex("\\") + 1:]
                print(lesson_name)

                if os.path.exists(destination_dir):

                    #check folder with that chapter number if doesn't exist
                    destination_full_path = destination_dir + "\\" + chapter

                    if os.path.exists(destination_full_path):
                        # if existcopy the file into that folder
                        print(f"{chapter} folder exists.")
                        shutil.copy(path_in_str, destination_full_path + "\\" + lesson_name)
                    else:
                        # create new folder
                        print(f"making folder {chapter}")
                        os.mkdir(destination_full_path)              

                else:
                    print(f"No such folder exists in {destination_dir}")
    else:
        print(f"No such folder exists in {file_path}")

if __name__ == "__main__":
    
    file_path = r"C:\Users\UserName\Downloads\Folder"
    file_type = ".py"
    file_keyword = "start"
    dir_keyword = "Chapter"
    destination_dir = r"C:\Users\UserName\Downloads\New"

    lesson_organizer(file_path, file_type, file_keyword, dir_keyword, destination_dir)