from pathlib import Path


#get current working directory
cwd = Path.cwd()
print(f'\nCurrent Working Directory\n{cwd}')

#full path name of a file
new_file_path = Path.joinpath(cwd, 'new_text.txt')
print(f'\nFull Path of a file\n{new_file_path}')

#Does file exist?
file_exist = Path.exists(new_file_path)
print(f'\nDoes file exist?\n{file_exist}')
