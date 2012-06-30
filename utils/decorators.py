import time
import inspect
from functools import wraps

def print_timing(func):
    """Print a function's execution time.
    Via http://www.daniweb.com/software-development/python/code/216610/timing-a-function-python"""
    @wraps(func)
    def wrapper(*arg, **kwarg):
        t1 = time.time()
        res = func(*arg, **kwarg)
        t2 = time.time()
        print '%s.%s took %0.3f ms' % (func.__module__, func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

def print_func_name(func):
    @wraps(func)
    def wrapper(*arg, **kwarg):
        print func.func_name
        res = func(*arg, **kwarg)
        return res
    return wrapper

def for_all_methods(decorator, name_matches=lambda func: True):
    """Decorate all methods of a class with decorator function.
    Via http://stackoverflow.com/a/6307868/477658"""
    def decorate(cls):
        for name, attr in cls.__dict__.items():
            if inspect.isfunction(attr) and name_matches(name):
                setattr(cls, name, decorator(attr))
        return cls
    return decorate

def cached_property(func):
    """Caches an object's property so expensive computations are only done once (such as DB lookups.)
    Example usage:

        class Example(object):
            @cached_property
            def big_range(self):
                return range(10000000)

        e = Example()
        e.big_range     # range is calculated, and stored in e.
        e.big_range     # Not calculated this time, just accesses the cached value.

    """
    @property
    def property_wrapper(obj):
        attribute_name = '_' + func.func_name
        if not hasattr(obj, attribute_name):
            setattr(obj, attribute_name, func(obj))
        return getattr(obj, attribute_name)
    return property_wrapper

