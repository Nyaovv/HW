from collections import namedtuple

def return_namedtuple(*args):
    names = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_res = func(*args, **kwargs)
            if isinstance(func_res, tuple):
                Point = namedtuple('Point', names)
                k = Point._make(func_res)
                #print(k)
                return k
            else:
                raise ValueError('Type is not tuple')
        return wrapper
    return decorator
