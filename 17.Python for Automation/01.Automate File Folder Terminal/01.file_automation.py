# read file and filter out only pass students
with open('../00.data/inputFile.txt', 'r') as file:

    # write the pass/fail lists
    pass_file = open("../00.data/pass_list.txt", "w")
    fail_file = open("../00.data/fail_list.txt", "w")

    for line in file:
        if line.split(" ")[2].strip("\n") == "P":
            pass_file.write(line)
        else:
            fail_file.write(line)

    pass_file.close()
    fail_file.close()
