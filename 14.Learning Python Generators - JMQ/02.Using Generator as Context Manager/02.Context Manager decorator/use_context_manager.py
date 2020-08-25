# Usage of Basic Context Manager

# using decorator of @contextmanager allows the function to have
# enter method
# exist method

from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1
        
        
        
class Some_Obj(object):
    def __init__(self, arg):
        self.some_property = arg
        
        
        
if __name__ == "__main__":
    obj = Some_Obj(5)
    print(obj.some_property)
    
    with simple_context_manager(obj):
        print(obj.some_property)
        
    print(obj.some_property)