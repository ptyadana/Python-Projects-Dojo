import numpy as np

def get_largest(lst):
        lst = np.array(lst)
        return lst.argsort()[-3:][::-1]
    
    
if __name__ == "__main__":
    lst = [1,2,3,4,5,8,3,4]
    print(get_largest(lst))