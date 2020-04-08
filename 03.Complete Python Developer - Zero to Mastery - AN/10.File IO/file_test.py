with open('test.txt', mode='r+') as my_file:
    
    print(my_file.readlines())
    text = my_file.write("ha ha ha.. this is funny joke.")
