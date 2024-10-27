def control(user_type):
    def dec(func):
        def wrap(user_type_1):
            if user_type_1 == user_type:
                return func(user_type_1)
            else:
                return 'denied'
        return wrap
    return dec

@control('admin')
def function(user_type):
    return 'admin'

print(function('admin'))
print(function('user'))