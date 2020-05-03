from pathlib import Path

# Get current directory
cwd = Path.cwd()

# Get the Parent Directory
parent = cwd.parent

#Is it a directory?
is_directory = Path.is_dir(parent)
print(f'\nIs it a directory?\n{is_directory}')

#Is it a file?
is_file = Path.is_file(parent)
print(f'\nIs it a file?\n{is_file}')

#List child directories
print(f'\n--- directory content ---\n')
for child in parent.iterdir():
    if child.is_dir():
        print(child)