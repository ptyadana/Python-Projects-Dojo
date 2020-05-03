stream = open('./output.txt', mode='wt')

print('\nCan I write to the file? ' + str(stream.writable()))

stream.write('H') #write char 'H'
stream.writelines(['ello', ' ', 'World!']) #write one or more strings or any objects whatever is iterable or iterators
stream.write('\n')

names = ['Richard', 'Vivian']
stream.writelines('\n'.join(names))

stream.close()