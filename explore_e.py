import multiprocessing
import time
from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 100

N = 8 * 1200  # 9600
NUM_CORES = 8

def compute_e_sequential(n_terms):
    e_approx = Decimal(0)
    
    for n in range(n_terms):
        print("First round:", n)
        e_approx += Decimal(1) / Decimal(factorial(n))  # Use math.factorial

    return e_approx

def compute_e_partial(start, end, queue):
    partial_sum = Decimal(0)

    fact = Decimal(1)
    for i in range(1, start):
        fact *= i 

    for n in range(start, end):
        print("Second round:", n)
        if n > 0:
            fact *= n 
        partial_sum += Decimal(1) / fact

    queue.put(partial_sum)

def compute_e_parallel(n_terms, num_cores):
    queue = multiprocessing.Queue()
    step = n_terms // num_cores
    processes = []

    for i in range(num_cores):
        start = i * step + 1  # 1 | 1001 | 2001 | ... | 7001
        end = (i + 1) * step if i < num_cores - 1 else n_terms  # 1000 | 2000 | 3000 | ... | 8000
        p = multiprocessing.Process(target=compute_e_partial, args=(start, end, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    e_approx = Decimal(0)
    while not queue.empty():
        e_approx += queue.get()

    return e_approx

if __name__ == "__main__": 
    start_time = time.time()
    e_sequential = compute_e_sequential(N)
    sequential_time = time.time() - start_time

    start_time = time.time()
    e_parallel = compute_e_parallel(N, NUM_CORES)
    parallel_time = time.time() - start_time

    print(f"Sequential e: {e_sequential}")
    print(f"Sequential Time: {sequential_time:.6f} sec")
    print(f"Parallel e: {e_parallel}")
    print(f"Parallel Time: {parallel_time:.6f} sec")
