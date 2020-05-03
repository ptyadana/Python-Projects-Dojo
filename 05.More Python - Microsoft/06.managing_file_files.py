from pathlib import Path

cwd = Path.cwd()

test_file = Path.joinpath(cwd, 'test.txt')

#get the file name
print(f'\nFile name\n{test_file.name}')

#get the extension
print(f'\nFile Suffix\n{test_file.suffix}')

#get the folder
print(f'\nFile folder\n{test_file.parent}')

#get the file size
print(f'\nFile size\n{test_file.stat().st_size}')
