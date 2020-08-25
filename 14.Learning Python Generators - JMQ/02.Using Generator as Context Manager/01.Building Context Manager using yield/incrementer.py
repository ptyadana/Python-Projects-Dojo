# increment some property by 1

from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property += 1
        yield
    finally:
        obj.some_property -= 1