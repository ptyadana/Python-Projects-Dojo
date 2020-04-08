from collections import Counter, defaultdict, OrderedDict

#Counter
my_list = [1,2,3,4,5,6,6,6]
print(Counter(my_list))

my_string = "hello I am think what to think. but it is quite hard."
print(Counter(my_string))

print("-------------------------------------------")
#defaultdic
my_dict = defaultdict(lambda: 'does not exist', {'a':100,'b':200})
print(my_dict['a'])
print(my_dict['c'])


print("-------------------------------------------")
#for normal dictionary, order doesn't matter. dic1 == dic2 will be True
#OrderedDict
dic1 = OrderedDict()
dic1['a'] = 100
dic1['b'] = 200

dic2 = OrderedDict()
dic2['b'] = 200
dic2['a'] = 100

print(dic1 == dic2)