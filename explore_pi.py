import threading
import multiprocessing
from queue import Queue
import time
from decimal import Decimal
from decimal import getcontext


def pi_serie_part(k_start, k_end, que=None):
    getcontext().prec = 100
    partial_sum = 0

    for k in range(k_start, k_end):
            partial_sum += Decimal(4) / (Decimal(2) * Decimal(k) * (Decimal(2) * Decimal(k) + Decimal(1)) * (Decimal(2) * Decimal(k) + Decimal(2))) * (Decimal(-1)) ** Decimal(k + 1)

    if que is not None:
        que.put(partial_sum)
    else:
        return partial_sum



qres = Queue()

N = 100000
threads_count = 8

num_cores = multiprocessing.cpu_count()
print(f"Number of cores: {num_cores}")
#
# getcontext().prec = 100
#
start_time = time.time()

# pool = multiprocessing.Pool(num_cores)
# results = pool.starmap(pi_serie_part, [(N*k+1, N*(k+1)) for k in range(threads_count)])
#
# for r in results:
#     qres.put(r)

# pi_serie_part(1, 2*N, qres)

thread_list = []
for i in range(threads_count):
    t = threading.Thread(target=pi_serie_part, args=(N*i+1, N*(i+1), qres))
    thread_list.append(t)
    t.start()

for t in thread_list:
    t.join()

end_time = time.time()

print(f"Threads finished. Elapsed time: {end_time - start_time}. {qres.qsize()} elements in queue.")

pi_approx = 0
while not qres.empty():
    pi_approx += qres.get()

pi_approx += 3

print(f"Pi approximation: {pi_approx}")