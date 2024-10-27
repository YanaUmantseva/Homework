def annotations(func):
    def wrap(**kwargs):
        ka = kwargs
        ann = func.__annotations__
        for key in ka:
            if type[key] != ann[key]:
                return 'Not correct'
        return func(**kwargs)



    return wrap



@annotations
def get_data(x: int, y:list, z:str):
    return x, y, z

print(get_data(x='2', y=(1,2), z=3))
