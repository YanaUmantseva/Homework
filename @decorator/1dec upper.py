def decorator(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrap

@decorator
def hello_world():
   return 'Hello world'

print(hello_world())






