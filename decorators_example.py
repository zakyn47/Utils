from funcy import decorator
import time

def log_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.2f} seconds to execute.")
        return result
    return wrapper

@log_time_decorator
def example_function():
    time.sleep(2)


example_function()