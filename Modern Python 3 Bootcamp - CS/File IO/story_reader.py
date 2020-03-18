#read
with open ('story.txt') as file:
    data = file.read()
    print(data)
file.closed