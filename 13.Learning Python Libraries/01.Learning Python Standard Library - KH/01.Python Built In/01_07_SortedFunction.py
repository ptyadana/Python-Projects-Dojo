# Least to Greatest
pointsInGame = [2, 4, -1, 0, -4, 10, -9]
sortedGame = sorted(pointsInGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))

print(sorted(["jerry", "Sue", "linda"]))

# Key Parameters
print(sorted("My favorite icecream is Vinilla".split(), key=str.upper))
print(sorted(pointsInGame, reverse=True))

leaderBoard = {
    123: "Jenny",
    673: "Linda",
    399: "Richard"
}
print(sorted(leaderBoard, reverse=True)) #normally sorted by key of dict

students = [("alice", "B", 12), ("eliza", "A", 16), ("ted", "C", 16)]
print(sorted(students, key=lambda student: student[0])) # sorting by name as key
print(sorted(students, key=lambda student: student[1])) # sorting by grade as key in ascending order
print(sorted(students, key=lambda student: student[2])) # sorting by age