#fix this code so that it prints a sorted list of all of our friends (alphabetical). 
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.append(new_friend[0])
print(friends)

friends.sort()

print(friends)

#====================================

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
print(friends)
new_friend = ['Stanley']

friends.extend(new_friend)
friends.sort()
print(friends)


