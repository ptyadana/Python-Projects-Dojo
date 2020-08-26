# this is a context manager

from contextlib import contextmanager
from logging import Logger, FileHandler

# a very simple example
#@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1

class Other_scm():
    def __init__(self, obj):
        self.obj = obj
    def __enter__(self):
        self.obj.some_property+=1
    def __exit__(self, *args):
        self.obj.some_property-=1

# a more complex example
@contextmanager
def error_logging(logger, level):
    oldlevel = logger.level
    try:
        logger.setLevel(level)
        yield
    finally:
        logger.setLevel(oldlevel)

if __name__ == "__main__":
    logger = Logger('name',20)
    handler = FileHandler('flog.log')
    logger.addHandler(handler)
    logger.info('this will get logged')
    with error_logging(logger, 30):
        logger.info('this will not get logged')
    logger.info('this will get logged because the level is {}'.format(logger.level))
    
class Simple_obj(object):
    def __init__(self, arg):
        self.some_property = arg
'''
s = Simple_obj(5)
with simple_context_manager(s):
    print s.some_property
    '''