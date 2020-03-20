#write
with open('newstory.txt','w') as file:
    file.writelines("Here is my new story.\n")
    file.writelines("Life is short, but amazing.\n")
    file.writelines("Never forget to enjoy and live the most out of it.")


#append
#don't allow seek to go back to the beginning of the file.
with open('newstory.txt','a') as file:
    file.writelines("\n\nThis is part 2 of my story.\n")
    file.writelines("Live in the moment of every seconds :).")


#read and append (allow seek to back to beginnig of file, or anywhere of the file to overwrite)
#always start to write at the beginning of the file
#only work with existing file
with open('newstory.txt','r+') as file:
    file.writelines("\"NEW STORY OF MY LIFE\"")
    # file.seek(130)
    # file.writelines('OPPPPP')