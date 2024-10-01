def catch_all_exceptions(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e) # To do logs, etc.
    return inner_function