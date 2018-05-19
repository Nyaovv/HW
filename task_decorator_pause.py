from functools import wraps
import time

def pause(se):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(se)
            return func(*args, **kwargs)
        return wrapper
    return decorator
