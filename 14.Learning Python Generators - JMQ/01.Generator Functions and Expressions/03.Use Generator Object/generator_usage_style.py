# with loop and generating on the fly
for num in (i for i in range(10)):
    print(num)
    
    
# generting using function
import even_integers_generators
for num in even_integers_generators.even_integers_function(10):
    print(num)
    
# together with other function
max_num = max(num for num in even_integers_generators.even_integers_function(100))
print(max_num)