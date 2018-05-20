from collections import namedtuple


def return_namedtuple(*args):
    pap = args
    def decorator(func):
        def wrapper(*args, **kwargs):
            fur = func(*args, **kwargs)
            if isinstance(fur, tuple):
                rofl = (pap)
                slov = {}
                taple = namedtuple('taple', rofl)
                for i in range(len(rofl)):
                    slov.update({rofl[i]:fur[i]})
                res = taple(**slov)
                return res
            else:
                return fur
            return func(*args, **kwargs)
        return wrapper
    return decorator
