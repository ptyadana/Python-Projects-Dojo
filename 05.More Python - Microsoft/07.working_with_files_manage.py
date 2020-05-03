stream = open('./manage.txt','wt')

#write the word demo! to the stream
stream.write('demo!')

#move back to the start of the file
stream.seek(0)

#write the word cool to the stream
stream.write('cool')

#flush the file stream contents to the buffer
stream.flush()

#flush the file stream and close the file
stream.close()
