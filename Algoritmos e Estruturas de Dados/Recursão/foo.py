# def fat(n):
#     if (n==0):
#         return 1
#     return (n*fat(n-1))

# fat(3) = 3 * fat(2) -> 3*2 = 6
#   fat(2) = 2 * fat (1) -> 2* 1 = 2
#       fat(1) = 1 * fat(0) -> 1*1 = 1
#           fat(0) = 1

# print(fib(7))

try:
    from line_profiler import LineProfiler

    def do_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

except ImportError:
    def do_profile(follow=[]):
        "Helpful if you accidentally leave in production!"
        def inner(func):
            def nothing(*args, **kwargs):
                return func(*args, **kwargs)
            return nothing
        return inner

def get_number():
    for x in range(5000000):
        yield x

def fib(n):
    if(n == 1 or n == 2):
        return 1
    return fib(n-1) + fib(n-2)

# @do_profile(follow=[get_number])
# def expensive_function():
#     for x in get_number():
#         i = x ^ x ^ x
#     return 'some result!'

@do_profile(follow=[fib])
def expensive_function():
    for x in fib(15):
        i = x ^ x ^ x
    return 'some result!'

result = expensive_function()