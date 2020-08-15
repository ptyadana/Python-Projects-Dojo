def convertString(lst):
    st = ""
    for index in range(len(lst) - 1):
        st += lst[index] + ", "
    
    return st + lst[len(lst) - 1]

def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    st = convertString(spam)
    print(st)

    #using python builtin join
    print(", ".join(spam))

if __name__ == "__main__":
    main()