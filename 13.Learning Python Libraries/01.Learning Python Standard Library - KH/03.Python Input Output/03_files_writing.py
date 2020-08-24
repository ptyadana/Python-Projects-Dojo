# Files and File Writing

# Open a file
myFile = open("data/test.txt", "w")

# w --> write
# r --> read
# r+ --> read and write
# a --> append

# Show attributes and properties of that file
print("Name: ", myFile.name)
print("Mode: ", myFile.mode)

# Write to a file
myFile.write("Today is a wonderful day.\nThe weather is getting cold.")
myFile.close()

# Read the file
newFile = open("data/test.txt", "r")
print("\nReading...", newFile.read(10)) #reading 10 characters of the file
print("\nReading...", newFile.read(10)) 
