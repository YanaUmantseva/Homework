import time

def log(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} секунд")
    return wrap


@log
def function():
    time.sleep(2)

print(function())

