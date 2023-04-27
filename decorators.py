# TODO: we could adjust this, so it returns all missing keywords instead of just the first one

def require_keywords(*required_keywords):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for keyword in required_keywords:
                if keyword not in kwargs:
                    raise ValueError(f"Missing required keyword argument: '{keyword}'")
            return func(*args, **kwargs)
        return wrapper
    return decorator
