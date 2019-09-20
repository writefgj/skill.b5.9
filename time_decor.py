import time

def time_this(num_runs):
    def decor(func):
        def wrap():
            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло {} секунд".format(avg_time))
        return wrap
    return decor

@time_this(num_runs=100)
def f():
    for j in range(1000000):
        pass

f()