import pprint

message = "Today is quite cloudy in Yangon. I just watched #Alive korean zombie moive which is pretty good."

count = {}

for character in message.upper():
    count.setdefault(character, 0) #if key doesn't exist in dict, set 0 as default value
    count[character] = count[character] + 1

#pprint.pprint(count)
text = pprint.pformat(count) #if we want the output string to do further manipulation 
print(text)