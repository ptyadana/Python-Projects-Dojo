import pickle
import os

#sort using sorted()
def sort_dictionary(dictionary):
    data = sorted(dictionary.items(), key=lambda  x: x[0])
    
    new_dict = {}
    for key,value in data:
        new_dict[key] = value
    
    return new_dict

def save_dictionary(dictionary, path):
    try:
        with open(path, "wb") as file:
            pickle.dump(dictionary, file)

    except Exception as e:
        print("Error saving the dictionary")
        print(e)


def load_dictionary(path):
    try:
        f_path = os.path.split(path)[0]
        if not os.path.isdir(f_path):
            print("file path is not valid!")
        else:
            with open(path, "rb") as file:
                return pickle.load(file)

    except Exception as e:
        print("Error in loading the dictionary.")
        print(e)

if __name__ == "__main__":
    my_dict = {
        "Water": "very important liquid for every living things",
        "Apple": "a delicious fruit",
        "Zero": "super wonderful maths item",
    }

    save_dictionary(sort_dictionary(my_dict), "./test/test_dict.pickle")
    loaded_dict = load_dictionary("./test/test_dict.pickle")
    print(loaded_dict)