# Basic Context Manager Framework

@contextmanager
def simple_context_manager(obj):
    try:
        # do something
        yield
    finally:
        # wrap up