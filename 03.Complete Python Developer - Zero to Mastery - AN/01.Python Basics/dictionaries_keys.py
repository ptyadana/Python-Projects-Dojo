#Dictionary Keys must be hashable : An object is said to be hashable if it has a hash value that remains the same during its lifetime. 
#which means immutable, such as int, string, booleans etc

dict = {
    123: [1,2,3],
    'A': "ABC",
    True: "hello",
}

print(dict[123])
print(dict['A'])
print(dict[True])