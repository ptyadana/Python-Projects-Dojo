# Tempfile Module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b"Save this special number for me: 234345") #writing as bytes string

tempFile.seek(0)
# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()