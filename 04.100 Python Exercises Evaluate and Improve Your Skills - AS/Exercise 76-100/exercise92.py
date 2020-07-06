# download the attached ZIP file and extract its files in a folder. 
# Then, write a script that counts and prints out the number of .py files in that folder.
import pathlib

count = 0;
for path in pathlib.Path('./92_files').iterdir():
    if path.is_file() and path.suffix == '.py':
        count += 1;

print(f'Number of files {count}');

#alternative way
# import glob

# file_list=glob.glob1("files","*.py")
# print(len(file_list))
