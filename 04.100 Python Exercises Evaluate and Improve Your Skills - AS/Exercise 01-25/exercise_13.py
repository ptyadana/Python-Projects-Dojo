# Question: Complete the script so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
# Hint: Use the map  function.
my_range = range(1, 21)

# Expected output: 
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  

# Answer:
# final_list =[str(item) for item in my_range]
# print(final_list)

final_list = list(map(str,my_range))
print(final_list)