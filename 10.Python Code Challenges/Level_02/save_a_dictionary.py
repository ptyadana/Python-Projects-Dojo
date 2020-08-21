# Challenge: save a dictionary for later use

"""
# Save dictionary, sorted by word
Input: dictionary to save, output file path

# Load dictionary
Input: file path to saved dictionary
Output: load the dictionary
"""

import os.path

SEPERATOR = " : "

#sort using list
def sort_dictionary(dictionary):
    lst = []
    new_dict = {}

    for word in dictionary.keys():
        lst.append(word)
    
    lst.sort()

    for word in lst:
        new_dict[word] = dictionary[word]
    
    return new_dict

def save_dictionary(dictionary, path):
    try:
        with open(path, "w") as f:
            for key, value in dictionary.items():
                f.writelines(key + SEPERATOR + value + "\n")

    except Exception as e:
        print("Error saving the dictionary")
        print(e)


def load_dictionary(path):
    try:
        new_dict = {}

        f_path = os.path.split(path)[0]
        if not os.path.isdir(f_path):
            print("file path is not valid!")
        else:
            with open(path, "r") as f:
                lines = f.readlines()

                for line in lines:
                    lst = line.split(SEPERATOR)
                    new_dict[lst[0]] = lst[1].strip("\n")
        
        return new_dict

    except Exception as e:
        print("Error in loading the dictionary.")
        print(e)

if __name__ == "__main__":
    my_dict = {
        "Water": "very important liquid for every living things",
        "Apple": "a delicious fruit",
        "Zero": "wonderful maths item",
    }

    # save_dictionary(sort_dictionary(my_dict), "./test/test_dict.txt")
    loaded_dict = load_dictionary("./test/test_dict.txt")
    print(loaded_dict)